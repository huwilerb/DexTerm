import os
from pydexcom import Dexcom, Region


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
