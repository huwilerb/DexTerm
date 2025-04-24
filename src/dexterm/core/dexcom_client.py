from typing import Optional, Protocol
from pydexcom import Dexcom
from enum import Enum
from ruamel.yaml import YAML, yaml_object


yaml = YAML()


@yaml_object(yaml)
class GlucoseUnit(str, Enum):
    mmol_l = "mmol_l"
    mg_dl = "mg_dl"

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(
            f"!{cls.__name__}",
            "{.name}".format(node),
        )

    @classmethod
    def from_yaml(cls, constructor, node):
        return cls[node.value]


@yaml_object(yaml)
class UserRegion(str, Enum):
    US = "us"
    OUS = "ous"
    JP = "jp"

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(
            f"!{cls.__name__}",
            "{.name}".format(node),
        )

    @classmethod
    def from_yaml(cls, constructor, node):
        return cls[node.value]


class Creditentials(Protocol):
    client_username: Optional[str]
    client_password: Optional[str]
    user_region: Optional[UserRegion]

    @property
    def is_valid(self) -> bool: ...


class DexcomClient:
    def __init__(self, creditentials: Creditentials) -> None:
        if not creditentials.is_valid:
            raise ValueError
        self.dexcom = Dexcom(
            username=creditentials.client_username,
            password=creditentials.client_password,  # type: ignore
            region=creditentials.user_region,  # type: ignore
        )

    def fetch_latest_glucose(self):
        return self.dexcom.get_current_glucose_reading()
