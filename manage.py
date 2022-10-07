import ast
import csv
import json

import click
import utm as utm
import uvicorn

from settings import PORT, HOST, ENVIRONMENT, BASE_DIR


@click.group()
def cli():
    pass


@cli.command()
def run_server():
    uvicorn.run(
        "commands.run_server:main_app",
        host=HOST,
        port=PORT,
        debug=(ENVIRONMENT == 'dev'),
        log_level="info",
    )


if __name__ == "__main__":
    cli()
