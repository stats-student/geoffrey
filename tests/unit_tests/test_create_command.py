import os
import pathlib
import pytest

from geoffrey import _create_command

## ############# ##
## CreateCommand ##
## ############# ##
def test_create_command_exists():
    assert "CreateCommand" in dir(_create_command)
    assert callable(_create_command.CreateCommand)


## ############## ##
## _validate_path ##
## ############## ##
def test_create_project_root_dir_no_name(tmp_path):
    os.chdir(tmp_path)

    cc = _create_command.CreateCommand("valid_path_placeholder")

    expected_msg = (
        "You passed an empty string/path as the project name. Please pass a valid name"
    )

    with pytest.raises(ValueError) as excinfo:
        cc._validate_path("")

    assert str(excinfo.value) == expected_msg


## ########### ##
## create_root ##
## ########### ##
@pytest.mark.parametrize("path", ["test_project", pathlib.Path("test_project")])
def test_create_project_root_dir(tmp_path, path):
    os.chdir(tmp_path)

    cc = _create_command.CreateCommand(path)

    cc.create_root(path)

    assert pathlib.Path("./test_project").exists()


@pytest.mark.parametrize(
    "path", ["dev/projects/test_project", pathlib.Path("dev/projects/test_project")]
)
def test_create_project_root_dir_with_parents(tmp_path, path):
    os.chdir(tmp_path)

    cc = _create_command.CreateCommand(path)

    cc.create_root(parents=True)

    assert pathlib.Path("./dev/projects/test_project").exists()


def test_create_project_root_folder_exists(tmp_path):
    os.chdir(tmp_path)
    cc = _create_command.CreateCommand("./test_project")

    os.mkdir("./test_project")

    expected_msg = "Folder test_project already exists. Please choose another name"

    with pytest.raises(FileExistsError) as excinfo:
        cc.create_root()

    assert str(excinfo.value) == expected_msg


def test_create_project_root_parents_false(tmp_path):
    os.chdir(tmp_path)

    cc = _create_command.CreateCommand("dev/projects/test_project")

    expected_msg = (
        f"Folder {pathlib.Path(cc.path)} has 1 or more parents that don't exist. Please create"
        f" these manually or pass parents=True to the create_root function"
    )

    with pytest.raises(FileNotFoundError) as excinfo:
        cc.create_root()

    assert str(excinfo.value) == expected_msg


## ############## ##
## create_subdirs ##
## ############## ##
def test_has_subdirs_attribute():
    cc = _create_command.CreateCommand("valid_path_placeholder")

    assert cc._subdirs == ["data_sources", "explorations", "models", "products"]


def test_subdirs_created(tmp_path):
    os.chdir(tmp_path)

    cc = _create_command.CreateCommand("valid_path_placeholder")

    cc.create_root()
    cc.create_subdirs()

    expected_dirs = sorted(["data_sources", "explorations", "models", "products"])
    actual_dirs = sorted(
        [i.stem for i in pathlib.Path("./valid_path_placeholder").glob("*/")]
    )

    assert expected_dirs == actual_dirs


## ############ ##
## create_files ##
## ############ ##
def test_files_created(tmp_path):
    os.chdir(tmp_path)

    cc = _create_command.CreateCommand("valid_path_placeholder")

    cc.create_root()
    cc.create_files()

    expected_files = sorted(["README.md", "project_scoping.md", ".geoff"])
    actual_files = sorted(
        [i.name for i in pathlib.Path("./valid_path_placeholder").glob("*/")]
    )

    assert expected_files == actual_files


## ########### ##
## create_tree ##
## ########### ##
@pytest.mark.parametrize("path", ["test_project", "path/to/test_project"])
def test_tree_build(path):
    cc = _create_command.CreateCommand(path)

    tree = cc.create_tree()

    expected_leaves = sorted(
        [
            "[gold1]\U0001F5BF [bold dodger_blue2]data_sources",
            "[gold1]\U0001F5BF [bold dodger_blue2]explorations",
            "[gold1]\U0001F5BF [bold dodger_blue2]models",
            "[gold1]\U0001F5BF [bold dodger_blue2]products",
            "[honeydew2]\U0001F5CB [spring_green2]README.md",
            "[honeydew2]\U0001F5CB [spring_green2]project_scoping.md",
        ]
    )

    actual_leaves = sorted([leaf.label for leaf in tree.children])

    assert tree.label == "test_project"
    assert expected_leaves == actual_leaves
