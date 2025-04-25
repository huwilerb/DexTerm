from typing import Optional, Protocol
from pydexcom import Dexcom
from ..utils.yaml_utils import YAMLSerializableEnum

from ruamel.yaml import YAML, yaml_object

yaml = YAML()


@yaml_object(yaml)
class GlucoseUnit(str, YAMLSerializableEnum):
    mmol_l = "mmol_l"
    mg_dl = "mg_dl"


@yaml_object(yaml)
class UserRegion(str, YAMLSerializableEnum):
    US = "us"
    OUS = "ous"
    JP = "jp"


class Credentials(Protocol):
    client_username: Optional[str]
    client_password: Optional[str]
    user_region: Optional[UserRegion]

    @property
    def is_valid(self) -> bool: ...


class DexcomClient:
    def __init__(self, credentials: Credentials) -> None:
        if not credentials.is_valid:
            raise ValueError
        self.dexcom = Dexcom(
            username=credentials.client_username,
            password=credentials.client_password,  # type: ignore
            region=credentials.user_region,  # type: ignore
        )

    def fetch_latest_glucose(self):
        return self.dexcom.get_current_glucose_reading()
