from pathlib import Path
import typer
from typing import Annotated, Optional
from rich import print

from dexterm.core.settings import get_settings, update_settings
from dexterm.core.config import SETTINGS_FILE_PATH
from dexterm.core.dexcom_client import GlucoseUnit, UserRegion

app = typer.Typer()
state = {"verbose": False}


@app.command()
def show():
    """Display the current settings"""
    settings = get_settings()
    print(settings)


@app.command()
def reset():
    """Reset the settings to default"""
    reset = typer.confirm("Are you sure you want to reset user settings ?")

    if not reset:
        typer.Abort()

    Path(SETTINGS_FILE_PATH).unlink(missing_ok=True)

    if state["verbose"]:
        print(f"""
        Removed settings file: {SETTINGS_FILE_PATH}
        Default will be used""")


@app.command()
def username(
    username: Annotated[Optional[str], typer.Argument()] = None,
    reset: Annotated[bool, typer.Option()] = False,
):
    """Update the client username. --reset to factory reset"""
    if reset:
        _username = None
    else:
        _username = username

    old_value, new_value = update_settings(
        "credentials",
        "client_username",
        _username,
    )

    if state["verbose"]:
        print(f"Update username from {old_value} to {new_value}")


@app.command()
def envfile(
    envfile: Annotated[
        Optional[Path],
        typer.Argument(
            help="Path to a env file containing credentials",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ] = None,
    reset: Annotated[bool, typer.Option()] = False,
):
    """Update the envfile. --reset to factory reset"""
    if reset:
        _envfile = None
    else:
        _envfile = str(envfile)

    old_value, new_value = update_settings(
        "credentials",
        "envfile_path",
        _envfile,
    )

    if state["verbose"]:
        print(f"Updated envfile from '{old_value}' to '{new_value}'")


@app.command()
def glucose_unit(
    glucose_unit: Annotated[
        Optional[GlucoseUnit],
        typer.Argument(help="Unit for the glucose reading."),
    ] = None,
    reset: Annotated[bool, typer.Option()] = False,
):
    """Update the glucose unit. --reset to factory reset"""
    if reset:
        _glucose_unit = GlucoseUnit.mg_dl
    else:
        _glucose_unit = glucose_unit

    old_value, new_value = update_settings(
        "metrics",
        "glucose_unit",
        _glucose_unit,
    )

    if state["verbose"]:
        print(f"Updated glucose_unit from {old_value} to {new_value}")


@app.command()
def user_region(
    user_region: Annotated[
        Optional[UserRegion],
        typer.Argument(help="Region of the user for Dexcom API"),
    ] = None,
    reset: Annotated[bool, typer.Option()] = False,
):
    """Update the user region. --reset to factory reset"""
    if reset:
        _user_region = None
    else:
        _user_region = user_region

    old_value, new_value = update_settings(
        "credentials",
        "user_region",
        _user_region,
    )

    if state["verbose"]:
        print(f"Updated glucose_unit from {old_value} to {new_value}")


@app.callback()
def main(verbose: bool = False):
    if verbose:
        state["verbose"] = True
