import os
from pydexcom import Dexcom, Region
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv


class DexcomClient:
    def __init__(self, env_file: Optional[Path] = None) -> None:
        if env_file:
            load_dotenv(env_file)

        username = os.getenv("DEXCOM_USERNAME")

        password = os.getenv("DEXCOM_PASSWORD")

        if username is None:
            msg = "No dexcom username found"
            raise ValueError(msg)
        if password is None:
            msg = "No dexcom password found"
            raise ValueError(msg)

        self.dexcom = Dexcom(
            username=username, password=password, region=Region.OUS)

    def get_glucose_level(self):
        return self.dexcom.get_current_glucose_reading()
