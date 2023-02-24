#!/usr/bin/env python
import typer
from autophotogram import __version__
from autophotogram.calibrate import Calibrate


# add the -h option for showing help
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


# creates the top-level autophotogram app
app = typer.Typer(add_completion=True, context_settings=CONTEXT_SETTINGS)


def version_callback(value: bool):
    "Adding a --version option to the CLI"
    if value:
        typer.echo(f"autophotogram {__version__}")
        raise typer.Exit()


def docs_callback(value: bool):
    "function to open docs"
    if value:
        # typer.echo("Opening https://eaton-lab.org/autophotogram in default browser")
        # typer.launch("https://eaton-lab.org/autophotogram")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True, help="print version and exit."),
    docs: bool = typer.Option(None, "--docs", callback=docs_callback, is_eager=True, help="Open documentation in browser."),
    ):
    """
    Call autophotogramit commands to access tools in the autophotogramit toolkit,
    and autophotogramit COMMAND -h to see help options for each tool
    (e.g., autophotogramit count -h)
    """
    typer.secho(
        f"autophotogramit (v.{__version__}): ...",
        fg=typer.colors.MAGENTA, bold=True,
    )


@app.command()
def calibrate(
    ):
    """
    """
    Calibrate()
