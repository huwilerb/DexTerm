from dataclasses import dataclass, field
from typing import Any, Literal, Optional, Tuple
from pathlib import Path
import os
import rich.repr
from dotenv import load_dotenv
from ruamel.yaml import YAML, yaml_object

from dexterm.core.config import SETTINGS_FILE_PATH
from dexterm.core.dexcom_client import GlucoseUnit, UserRegion


yaml = YAML()


@yaml_object(yaml)
@dataclass
class Credentials:
    """Store all crendentials settings and logic"""

    envfile_path: Optional[str] = None
    client_username: Optional[str] = None
    client_password: Optional[str] = None
    user_region: Optional[UserRegion] = None

    def __post_init__(self):
        self.load_from_dotenv()

    def load_from_dotenv(self) -> None:
        if self.envfile_path is None:
            return
        if Path(self.envfile_path).exists():
            load_dotenv(self.envfile_path)
            username = os.getenv("DEXTERM_USERNAME")
            password = os.getenv("DEXTERM_PASSWORD")
        else:
            msg = f"Provided envfile do not exists: {self.envfile_path}"
            raise FileNotFoundError(msg)

        if username is not None:
            self.client_username = username
        if password is not None:
            self.client_password = password

    @property
    def is_valid(self) -> bool:
        if self.client_username is None:
            return False
        if self.client_password is None:
            return False
        if self.user_region is None:
            return False

        return True


@yaml_object(yaml)
@dataclass
class Metrics:
    """Store all metrics settings"""

    glucose_unit: GlucoseUnit = GlucoseUnit.mg_dl


@yaml_object(yaml)
@dataclass
class Settings:
    credentials: Credentials = field(default_factory=Credentials)
    metrics: Metrics = field(default_factory=Metrics)

    def __rich_repr__(self) -> rich.repr.Result:
        envfile_path = self.credentials.envfile_path
        if envfile_path is None:
            yield "Env file set", False
        else:
            yield "Env file set", True
            yield "Env file path", envfile_path
            yield "Env file exists", Path(envfile_path).exists()

        username = self.credentials.client_username
        if username is None:
            yield "Username set", False
        else:
            yield "Username set", True
            yield "Username value", username

        yield "Password set", self.credentials.client_password is not None

        user_region = self.credentials.user_region
        if user_region is None:
            yield "User region set", False
        else:
            yield "User region set", True
            yield "User region value", user_region.value

        yield "Credentails validity", self.credentials.is_valid
        yield "Glucose unit value", self.metrics.glucose_unit.value


def write_user_settings(settings: Settings) -> None:
    with SETTINGS_FILE_PATH.open("w") as f:
        yaml.dump(settings, f)


def get_settings() -> Settings:
    """Get the settings as an object"""
    if not SETTINGS_FILE_PATH.exists():
        return Settings()
    with SETTINGS_FILE_PATH.open("r") as f:
        data = yaml.load(f)

    if data is None:
        return Settings()
    else:
        return data


def update_settings(
    componant: Literal["credentials", "metrics"],
    key: str,
    new_value: Any,
) -> Tuple[Any, Any]:
    """Update a key of settings"""

    settings = get_settings()
    comp = getattr(settings, componant, None)
    if comp is None:
        raise ValueError

    value = getattr(comp, key, "key_error")

    if value == "key_error":
        raise ValueError

    setattr(comp, key, new_value)
    setattr(settings, componant, comp)

    write_user_settings(settings)

    return (value, new_value)


if __name__ == "__main__":
    settings = get_settings()
    print(settings)
