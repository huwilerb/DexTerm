import typer

app = typer.Typer()


@app.command()
def status():
    """Display the status of the data fetching process"""
    typer.echo("Data fetching process is ?")


@app.command()
def current():
    """Display the current CGM value"""
    typer.echo("Your glucose is ?")
