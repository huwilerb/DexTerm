import typer
from dexterm.cli.glucose import app as glucose_app

help_message = "A CLI tool to keep track of your blood sugar level"

app = typer.Typer(help=help_message)

app.add_typer(glucose_app, name="glucose")
