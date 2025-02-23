import json
from typing import Optional
from dexterm.core.config import GLUCOSE_FILE_PATH


def read_glucose_data() -> Optional[dict]:
    """Read the cached glucose file"""

    if GLUCOSE_FILE_PATH.exists():
        with GLUCOSE_FILE_PATH.open("r") as file:
            return json.load(file)

    return None


def write_glucose_data(data: dict) -> None:
    """Write the glucose data to file"""
    with GLUCOSE_FILE_PATH.open("w") as file:
        json.dump(data, file)
