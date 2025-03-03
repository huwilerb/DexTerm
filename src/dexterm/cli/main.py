import typer
from dexterm.cli import glucose
from dexterm.cli import settings


help_message = "A CLI tool to keep track of your blood sugar level"

app = typer.Typer(help=help_message)

app.add_typer(glucose.app, name="glucose")
app.add_typer(settings.app, name="settings")

if __name__ == "__main__":
    app()
