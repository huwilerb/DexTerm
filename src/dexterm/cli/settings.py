from pathlib import Path
from typing import Optional
from click import Choice
import typer
from rich import print
from typing_extensions import Annotated

from dexterm.core.settings import write_user_settings, get_settings
from dexterm.core.config import SETTINGS_FILE_PATH
from dexterm.core.dexcom_client import GlucoseUnit

app = typer.Typer()

settings = get_settings()


@app.command()
def status():
    """Display the current status of the settings"""
    print(settings)


@app.command()
def set(
    username: Annotated[str, typer.Option(help="Username for dexcom API")] = "",
    password: Annotated[
        str, typer.Option(help="Password for dexom API", hide_input=True)
    ] = "",
    envfile: Annotated[
        str, typer.Option(help="Path to a env file containing creditentials")
    ] = "",
    glucose_unit: Annotated[
        Optional[GlucoseUnit],
        typer.Option(help="Unit for the glucose reading."),
    ] = None,
):
    if username != "":
        settings.client_username = username

    if password != "":
        settings.client_password = password

    if envfile != "":
        settings.envfile_path = envfile

    if glucose_unit is not None:
        settings.glucose_unit = glucose_unit

    write_user_settings(settings)
    settings.export_to_env()


@app.command()
def reset():
    reset = typer.confirm("Are you sure you want to reset user settings ?")

    if not reset:
        typer.Abort()

    Path(SETTINGS_FILE_PATH).unlink(missing_ok=True)
