import logging
import pathlib
import typer


logger = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def data_source(
    name: str,
    database_source: bool = typer.Option(False, "--database", "-d"),
    extract_source: bool = typer.Option(False, "--extract", "-e"),
    web_source: bool = typer.Option(False, "--web-download", "-w")
):
    """
    Adds a data source folder called NAME in the data_sources
    directory
    """
    if pathlib.Path(".geoff").exists():
        logger.info(f"adding data source {name}")
        pathlib.Path(f"data_sources/{name}").mkdir()
    else:
        raise RuntimeError(
            "This directory isn't managed by geoff. Please change to a directory that is"
        )


@app.command()
def exploration():
    """
    Adds an exploration to the data_sources folder
    """
    pass


@app.command()
def model():
    """
    Adds a model to the data_sources folder
    """
    pass


@app.command()
def product():
    """
    Adds a product to the data_sources folder
    """
    pass
