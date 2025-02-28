from pathlib import Path

from platformdirs import user_cache_dir, user_config_dir, user_state_dir

APP_NAME = "dexterm"
CONFIG_DIR = Path(user_config_dir(APP_NAME, ensure_exists=True))
CACHE_DIR = Path(user_cache_dir(APP_NAME, ensure_exists=True))
STATE_DIR = Path(user_state_dir(APP_NAME, ensure_exists=True))

GLUCOSE_FILE = "glucose_data.json"
STATE_FILE = "update_state.json"
SETTINGS_FILE = "settings.json"

GLUCOSE_FILE_PATH = CACHE_DIR.joinpath(GLUCOSE_FILE)
STATE_FILE_PATH = STATE_DIR.joinpath(STATE_FILE)
SETTINGS_FILE_PATH = CONFIG_DIR.joinpath(SETTINGS_FILE)


CLIENT_UPDATE_INTERVAL_MINUTES = 5
