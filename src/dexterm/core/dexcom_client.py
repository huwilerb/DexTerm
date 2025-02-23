import os
from pydexcom import Dexcom, Region
from pathlib import Path
from typing import Optional


class DexcomClient:
    def __init__(self, env_file: Optional[Path] = None) -> None:
        username = os.getenv("DEXCOM_USERNAME")  # TODO: Handle None values
        password = os.getenv("DEXCOM_PASSWORD")  # TODO: Handle None values
        self.dexcom = Dexcom(username=username, password=password, region=Region.OUS)

    def get_glucose_level(self):
        return self.dexcom.get_current_glucose_reading()
