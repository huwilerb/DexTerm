import typer

from dexterm.core.data import read_glucose_data, update_glucose_data
from typing_extensions import Annotated

from dexterm.core.settings import get_settings


app = typer.Typer()


@app.command()
def status():
    """Display the status of the data fetching process"""
    data = read_glucose_data()
    typer.echo(data)


@app.command()
def current():
    """Display the current CGM value"""
    data = read_glucose_data()
    typer.echo(data)


@app.command()
def update(
    print_result: Annotated[
        bool, typer.Option(help="Print the results once finished")
    ] = False,
    password: Annotated[
        str, typer.Option(help="Pass the password to the settings")
    ] = "",
):
    """Update the CGM value to cache"""
    settings = get_settings()

    if password != "":
        settings.creditentials.client_password = password

    data = update_glucose_data(settings)

    if print_result:
        typer.echo(data)
