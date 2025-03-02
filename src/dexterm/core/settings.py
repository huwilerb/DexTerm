from dataclasses import dataclass
from typing import Optional
from pathlib import Path
import os
import rich.repr
from dotenv import load_dotenv
from ruamel.yaml import YAML, yaml_object

from dexterm.core.config import SETTINGS_FILE_PATH
from dexterm.core.dexcom_client import GlucoseUnit


yaml = YAML()


@yaml_object(yaml)
@dataclass
class Settings:
    envfile_path: Optional[str] = None
    client_username: Optional[str] = None
    client_password: Optional[str] = None
    glucose_unit: GlucoseUnit = GlucoseUnit.mg_dl

    def __post_init__(self):
        self.export_to_env()

    def export_to_env(self) -> None:
        if self.envfile_path is not None:
            load_dotenv(self.envfile_path)
        if self.client_username is not None:
            os.environ["DEXTERM_USERNAME"] = self.client_username
        if self.client_password is not None:
            os.environ["DEXTERM_PASSWORD"] = self.client_password

    def __rich_repr__(self) -> rich.repr.Result:
        if self.envfile_path is None:
            yield "Env file set", False
        else:
            yield "Env file set", True
            yield "Env file path", self.envfile_path
            yield "Env file exists", Path(self.envfile_path).exists()

        if self.client_username is None:
            yield "Username set", False
        else:
            yield "Username set", True
            yield "Username value", self.client_username

        yield "Password set", self.client_password is not None

        yield "Glucose unit", self.glucose_unit


def write_user_settings(settings: Settings) -> None:
    with SETTINGS_FILE_PATH.open("w") as f:
        yaml.dump(settings, f)


def get_settings() -> Settings:
    """Get the settings as an object"""
    with SETTINGS_FILE_PATH.open("r") as f:
        data = yaml.load(f)

    if data is None:
        return Settings()
    else:
        return data
