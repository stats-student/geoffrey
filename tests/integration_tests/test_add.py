import filecmp
import os
import pathlib
import pytest

from typer.testing import CliRunner

from geoffrey.add import app


runner = CliRunner()

@pytest.fixture()
def create_root(tmp_path):
    os.chdir(tmp_path)

    for folder in ["data_sources", "explorations", "models", "products"]:
        os.mkdir(folder)
    
    for file in ["README.md", "project_scoping.md", ".geoff"]:
        open(file, "a").close()
    
    yield

@pytest.mark.parametrize("command", ["data-source", "exploration", "model", "product"])
def test_commands_exist(command):
    result = runner.invoke(app, [command, "--help"])
    assert result.exit_code == 0

## ############### ##
## add data-source ##
## ############### ##
def test_add_data_source_creates_folder(create_root):
    result = runner.invoke(app, ["data-source", "test_data_source"])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_data_source").exists()

def test_add_data_source_non_geoff_directory(create_root):
    os.chdir("..")

    result = runner.invoke(app, ["data-source", "test_data_source"])

    assert result.exc_info[0] == RuntimeError
    assert str(result.exc_info[1]) == (
        "This directory isn't managed by geoff. Please change to a directory that is"
    )

@pytest.mark.parametrize("option", ["--database", "-d"])
def test_add_database_data_source_folder_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_db_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_db_data_source").exists()

@pytest.mark.parametrize("option", ["--extract", "-e"])
def test_add_extract_data_source_folder_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_db_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_db_data_source").exists()

@pytest.mark.parametrize("option", ["--web-download", "-w"])
def test_add_web_download_data_source_folder_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_db_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_db_data_source").exists()

@pytest.mark.parametrize("option", ["--database", "-d"])
def test_database_source_files_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_db_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path(
        "./data_sources/test_db_data_source/test_db_data_source_metadata.md"
    ).exists()
    assert filecmp.cmp(
        "./data_sources/test_db_data_source/test_db_data_source_metadata.md",
        "../../geoffrey/templates/data_sources/metadata.md"
    )
