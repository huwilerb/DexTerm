import json
from typing import Optional
from dexterm.core.config import GLUCOSE_FILE_PATH
from dexterm.core.dexcom_client import DexcomClient


def read_glucose_data() -> Optional[dict]:
    """Read the cached glucose file"""

    if GLUCOSE_FILE_PATH.exists():
        with GLUCOSE_FILE_PATH.open("r") as file:
            return json.load(file)

    return None


def update_glucose_data() -> Optional[dict]:
    """Update the glucose data in cache"""
    client = DexcomClient()
    data = client.fetch_latest_glucose()
    if data:
        data_dict = data.json
        write_glucose_data(data_dict)
        return data_dict
    else:
        return None


def write_glucose_data(data: dict) -> None:
    """Write the glucose data to file"""
    with GLUCOSE_FILE_PATH.open("w") as file:
        json.dump(data, file)
