import logging
import pathlib
import rich
import shutil
import typer

from rich.tree import Tree

from .add_commands._add_data_source_command import AddDataSourceCommand


logger = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def data_source(
    name: str,
    database_source: bool = typer.Option(False, "--database", "-d"),
    extract_source: bool = typer.Option(False, "--extract", "-e"),
    web_source: bool = typer.Option(False, "--web-download", "-w"),
):
    """
    Adds a data source folder called NAME in the data_sources
    directory
    """
    ads = AddDataSourceCommand(f"{name}")

    if ads.check_is_geoff_dir():
        logger.info(f"adding data source {ads.name}")
        ads.create_dir()

        if database_source:
            ads.copy_templates("db_metadata.md")
        
        elif extract_source:
            ads.copy_templates("extract_metadata.md")
            
        elif web_source:
            ads.copy_templates("web_metadata.md")
            
        else:
            ads.copy_templates("empty_metadata.md")

        ads.replace_placeholders()

        tree = ads.create_tree()

        print(f"\U0001FA3F {name} added!\n")
        rich.print(tree)

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
