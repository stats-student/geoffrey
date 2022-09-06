import logging
import pathlib
import rich
import shutil
import typer

from rich.tree import Tree


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
    if pathlib.Path(".geoff").exists():
        logger.info(f"adding data source {name}")
        pathlib.Path(f"data_sources/{name}").mkdir()

        if database_source:
            metadata_template = (
                pathlib.Path(__file__).parent / "templates/data_sources/db_metadata.md"
            )
        elif extract_source:
            metadata_template = (
                pathlib.Path(__file__).parent
                / "templates/data_sources/extract_metadata.md"
            )
        elif web_source:
            metadata_template = (
                pathlib.Path(__file__).parent / "templates/data_sources/web_metadata.md"
            )
        else:
            metadata_template = (
                pathlib.Path(__file__).parent
                / "templates/data_sources/empty_metadata.md"
            )

        logger.info(f"Copying {metadata_template.name} to data_sources folder")
        shutil.copy(str(metadata_template), str(f"data_sources/{name}/metadata.md"))

        with open(f"data_sources/{name}/metadata.md", "r") as md:
            contents = md.read()
            contents = contents.replace("<-project_name->", name)

        with open(f"data_sources/{name}/metadata.md", "w") as md:
            md.write(contents)

        tree = Tree("[gold1]\U0001F5BF [bold dodger_blue2]data_sources")
        tree_ds = tree.add(f"[gold1]\U0001F5BF [bold dodger_blue2]{name}")
        tree_ds.add("[honeydew2]\U0001F5CB [spring_green2]metadata.md")

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
