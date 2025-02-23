import typer
from dexterm.cli.glucose import app as glucose_app

app = typer.Typer()
app.add_typer(glucose_app, name="glucose")
