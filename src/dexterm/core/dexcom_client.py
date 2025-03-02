import os
from pydexcom import Dexcom, Region
from enum import Enum
from ruamel.yaml import YAML, yaml_object

yaml = YAML()


class DexcomClient:
    def __init__(self) -> None:
        username = os.getenv("DEXTERM_USERNAME")

        password = os.getenv("DEXTERM_PASSWORD")

        if username is None:
            msg = "No dexcom username found"
            raise ValueError(msg)
        if password is None:
            msg = "No dexcom password found"
            raise ValueError(msg)

        self.dexcom = Dexcom(
            username=username, password=password, region=Region.OUS)

    def fetch_latest_glucose(self):
        return self.dexcom.get_current_glucose_reading()


@yaml_object(yaml)
class GlucoseUnit(str, Enum):
    mmol_l = "mmol_l"
    mg_dl = "mg_dl"

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(f"!{cls.__name__}", "{.name}".format(node))

    @classmethod
    def from_yaml(cls, constructor, node):
        return cls[node.value]
