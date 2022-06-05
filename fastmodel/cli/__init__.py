import click
import uvicorn

from fastmodel.__about__ import __version__


@click.group()
@click.help_option("-h", "--help")
@click.version_option(__version__, "-v", "--version", prog_name="fastmodel")
def cli():
    pass


@cli.command(help="Run the HTTP server.")
def serve():
    uvicorn.run(
        "fastmodel.http:router",
        host="127.0.0.1",
        port=8000,
        log_level="info",
    )
