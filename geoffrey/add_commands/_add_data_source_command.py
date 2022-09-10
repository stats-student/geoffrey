"""
This script contains all the functions required for the add data source command

Author: Daniel Yates
"""
import logging
import pathlib
import shutil

from rich.tree import Tree

from ._add_base_command import AddCommand

logger = logging.getLogger(__name__)


class AddDataSourceCommand(AddCommand):
    def __init__(self, name: str) -> None:
        """
        Parameters
        ----------
        name: The name of the data source to create

        Attributes
        ----------
        name: The name of the data source to create
        """
        self.name = name

        super().__init__(
            "data_sources",
            self.name
        )
    
    def copy_templates(self, template_name: str):
        """
        Copies metadata template files to the data source directory

        Parameters
        ----------
        template_name: The name of the required template file
        """
        self.metadata_template = (
            pathlib.Path(__file__).parent.parent
            / f"templates/data_sources/{template_name}"    
        )

        logger.info(
            f"copying metadata template from {self.metadata_template.resolve()}"
        )
        shutil.copy(
            str(self.metadata_template),
            str(f"data_sources/{self.name}/metadata.md")
        )

    def replace_placeholders(self) -> None:
        with open(f"data_sources/{self.name}/metadata.md", "r") as md:
            contents = md.read()
            contents = contents.replace("<-project_name->", self.name)

        with open(f"data_sources/{self.name}/metadata.md", "w") as md:
            md.write(contents)

    def create_tree(self) -> Tree:
        tree = Tree("[gold1]\U0001F5BF [bold dodger_blue2]data_sources")
        tree_ds = tree.add(f"[gold1]\U0001F5BF [bold dodger_blue2]{self.name}")
        tree_ds.add("[honeydew2]\U0001F5CB [spring_green2]metadata.md")

        return tree