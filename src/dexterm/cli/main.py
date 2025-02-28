import typer
from dexterm.cli.glucose import app as glucose_app
from dexterm.cli.settings import app as settings_app


help_message = "A CLI tool to keep track of your blood sugar level"

app = typer.Typer(help=help_message)

app.add_typer(glucose_app, name="glucose")
app.add_typer(settings_app, name="settings")

if __name__ == "__main__":
    app()
