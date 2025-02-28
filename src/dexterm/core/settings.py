from dataclasses import dataclass
from typing import Optional
from pathlib import Path
import yaml
import os
import rich.repr
from dotenv import load_dotenv

from dexterm.core.config import SETTINGS_FILE_PATH


@dataclass
class Settings:
    envfile_path: Optional[str] = None
    client_username: Optional[str] = None
    client_password: Optional[str] = None

    def __post_init__(self):
        self.export_to_env()

    def export_to_env(self) -> None:
        if self.envfile_path is not None:
            load_dotenv(self.envfile_path)
        if self.client_username is not None:
            print(self.client_username)
            os.environ["DEXTERM_USERNAME"] = self.client_username
        if self.client_password is not None:
            print(self.client_password)
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


def load_user_settings() -> dict:
    """read the user settings as dict"""
    if SETTINGS_FILE_PATH.exists():
        with SETTINGS_FILE_PATH.open("r") as file:
            return yaml.safe_load(file)
    return {}


def write_user_settings(settings: Settings) -> None:
    keys = ["envfile_path", "client_username"]

    data = {key: getattr(settings, key) for key in keys}
    data = {k: v for k, v in data.items() if v is not None}

    with SETTINGS_FILE_PATH.open("w") as file:
        yaml.safe_dump(data, file)


def get_settings() -> Settings:
    """Get the settings as an object"""
    data = load_user_settings()
    return Settings(**data)
