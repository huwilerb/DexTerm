import datetime
import json
from typing import Optional
from dexterm.core.config import GLUCOSE_FILE_PATH
from dexterm.core.dexcom_client import DexcomClient
from dexterm.core.settings import (
    Credentials,
    Metrics,
    GlucoseUnit,
    Settings,
)
from pydexcom import GlucoseReading


def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


def read_glucose_data() -> Optional[dict]:
    """Read the cached glucose file"""

    if GLUCOSE_FILE_PATH.exists():
        with GLUCOSE_FILE_PATH.open("r") as file:
            return json.load(file)

    return None


def transform_reading_data(metrics: Metrics, data: GlucoseReading) -> dict:
    """Transform the reading with specific metrics"""
    results = {}

    results["DT"] = data.datetime
    results["WT"] = datetime.datetime.now()
    results["Unit"] = metrics.glucose_unit

    if metrics.glucose_unit == GlucoseUnit.mg_dl:
        results["Value"] = data.mg_dl
    elif metrics.glucose_unit == GlucoseUnit.mmol_l:
        results["Value"] = data.mmol_l

    results["Trend"] = data.trend
    results["Trend_arrow"] = data.trend_arrow

    return results


def fetch_latest_glucose(creditentials: Credentials) -> GlucoseReading:
    """Fetch the latest glucose reading from API"""
    client = DexcomClient(creditentials)
    data = client.fetch_latest_glucose()
    if data is None:
        msg = "The API didn't returned any data"
        raise ValueError(msg)
    return data


def update_glucose_data(settings: Settings) -> dict:
    """Update the glucose data in cache"""

    glucose_data = fetch_latest_glucose(settings.credentials)
    formated_data = transform_reading_data(settings.metrics, glucose_data)
    write_glucose_data(formated_data)

    return formated_data


def write_glucose_data(data: dict) -> None:
    """Write the glucose data to file"""
    with GLUCOSE_FILE_PATH.open("w") as file:
        json.dump(data, file, default=serialize_datetime)
