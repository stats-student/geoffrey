import logging
import pathlib
import rich
import typer

from rich.progress import Progress
from rich.tree import Tree

from . import add
from ._create_command import CreateCommand


logger = logging.getLogger(__name__)

app = typer.Typer()
app.add_typer(add.app, name="add")


@app.command()
def create(name: str, parents: bool = False):
    """
    Create a project called NAME.

    If --parents is used, the parent directories in NAME will be created
    if they don't already exist.
    """
    project_path = pathlib.Path(name)
    logger.debug(f"Creating directory at {project_path.resolve()}")

    cc = CreateCommand(project_path)

    cc.create_root(parents=parents)
    cc.create_subdirs()
    cc.create_files()

    print(f"\U0001F680 {project_path.stem} created!\n")

    tree = cc.create_tree()

    rich.print(tree)


if __name__ == "__main__":
    app()
