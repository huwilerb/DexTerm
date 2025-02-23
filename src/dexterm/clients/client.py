from pathlib import Path
from typing import Optional, Protocol


class Client(Protocol):
    env_file: Optional[Path]

    def fetch_latest_glucose(self) -> None: ...
    """Fetch the latest glucose value to cache"""
