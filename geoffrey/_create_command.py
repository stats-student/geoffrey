"""
This script contains all the functions required for the create command.

Author: Daniel Yates
"""
import logging
import pathlib
import shutil

from rich.tree import Tree
from typing import Union

logger = logging.getLogger(__name__)


class CreateCommand:
    def __init__(self, path: Union[str, pathlib.Path]) -> None:
        """
        Parameters
        ----------
        path: The new location to create for the project

        Attributes
        ----------
        _subdirs: The subdirs to be created
        """
        self._subdirs = ["data_sources", "explorations", "models", "products"]
        self.path = self._validate_path(path)

    def _validate_path(self, path: Union[str, pathlib.Path]) -> pathlib.Path:
        """
        Checks if the path is either an empty string or a pathlib.Path instance pointing
        to the current directory '.' then converts the path to a pathlib.Path.

        Parameters
        ----------
        path: The new location to create for the project
        """
        empty_string_check: bool = isinstance(path, str) & (path == "")
        empty_path_check: bool = isinstance(path, pathlib.Path) & (
            path == pathlib.Path(".")
        )

        logger.debug(
            f"empty_string_check = {empty_string_check}\nempty_path_check = {empty_path_check}"
        )

        if empty_string_check or empty_path_check:
            raise ValueError(
                "You passed an empty string/path as the project name. Please pass a valid name"
            )
        else:
            return pathlib.Path(path)

    def create_root(self, parents: bool = False) -> None:
        """
        Creates the root folder for the new project.

        Parameters
        ----------
        parents: Passed directly to pathlib.Path.mkdir(). Whether to create parent
                 directories (if applicable)
        """
        logger.info(f"Creating project root at {self.path}")

        try:
            self.path.mkdir(parents=parents)

        except FileExistsError:
            raise FileExistsError(
                f"Folder {self.path} already exists. Please choose another name"
            )

        except FileNotFoundError:
            raise FileNotFoundError(
                (
                    f"Folder {self.path} has 1 or more parents that don't exist. Please create"
                    f" these manually or pass parents=True to the create_root function"
                )
            )

    def create_subdirs(self) -> None:
        """
        Creates the subdirectories in self.path folder
        """
        for subdir in self._subdirs:
            logger.info(f"Creating project sub directory: {subdir}")

            (self.path / subdir).mkdir()

    def create_files(self) -> None:
        """
        Creates the files for the self.path folder
        """
        # Create empty .geoff file
        open(self.path / ".geoff", "a").close()

        for file in (pathlib.Path(__file__).parent / "templates/root").glob("*"):
            logger.info(f"Copying {file.name} to root folder")

            shutil.copy(str(file), str(self.path) + "/" + str(file.name))

    def create_tree(self) -> Tree:
        """
        Creates a tree to display what folders and files have been
        created
        """
        tree = Tree(self.path.stem)
        _ = tree.add("[gold1]\U0001F5BF [bold dodger_blue2]data_sources")
        _ = tree.add("[gold1]\U0001F5BF [bold dodger_blue2]explorations")
        _ = tree.add("[gold1]\U0001F5BF [bold dodger_blue2]models")
        _ = tree.add("[gold1]\U0001F5BF [bold dodger_blue2]products")
        _ = tree.add("[honeydew2]\U0001F5CB [spring_green2]README.md")
        _ = tree.add("[honeydew2]\U0001F5CB [spring_green2]project_scoping.md")

        return tree
