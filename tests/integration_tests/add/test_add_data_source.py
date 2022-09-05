import filecmp
import os
import pathlib
import pytest

from typer.testing import CliRunner

from geoffrey.add import app


runner = CliRunner()


@pytest.mark.parametrize("command", ["data-source", "exploration", "model", "product"])
def test_commands_exist(command):
    result = runner.invoke(app, [command, "--help"])
    assert result.exit_code == 0


## ######### ##
## No option ##
## ######### ##
def test_add_data_source_no_options_folder_created(create_root):
    result = runner.invoke(app, ["data-source", "test_data_source"])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_data_source").exists()

def test_add_data_source_no_options_files_created(create_root):
    result = runner.invoke(app, ["data-source", "test_data_source"])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_data_source/metadata.md").exists()

def test_add_data_source_no_options_empty_template(create_root):
    result = runner.invoke(app, ["data-source", "test_data_source"])

    assert result.exit_code == 0
    with open("./data_sources/test_data_source/metadata.md", "r") as md:
        md_contents = md.read()
        assert md_contents == "# test_data_source metadata"

def test_add_data_source_no_options_output_printed(create_root):
    result = runner.invoke(app, ["data-source", "test_data_source"])

    expected_output = """
🖿 data_sources
├── 🖿 test_data_sources
└── 🗋 metadata.md
    """ 
    expected_output in result.stdout

## ######## ##
## Database ##
## ######## ##
@pytest.mark.parametrize("option", ["--database", "-d"])
def test_add_database_data_source_folder_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_db_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_db_data_source").exists()

@pytest.mark.parametrize("option", ["--database", "-d"])
def test_database_source_files_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_db_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_db_data_source/metadata.md").exists()

@pytest.mark.parametrize("option", ["--database", "-d"])
def test_database_source_files_placeholders_replaced(create_root, option):
    result = runner.invoke(app, ["data-source", "test_db_data_source", option])

    assert result.exit_code == 0
    with open("./data_sources/test_db_data_source/metadata.md", "r") as md:
        md_contents = md.read()
        assert "<-project_name->" not in md_contents
        assert "# test_db_data_source metadata" in md_contents

@pytest.mark.parametrize("option", ["--database", "-d"])
def test_add_data_source_db_output_printed(create_root, option):
    result = runner.invoke(app, ["data-source", "test_db_data_source", option])

    expected_output = """
🖿 data_sources
├── 🖿 test_db_data_sources
└── 🗋 metadata.md
    """ 
    expected_output in result.stdout

## ####### ##
## Extract ##
## ####### ##
@pytest.mark.parametrize("option", ["--extract", "-e"])
def test_add_extract_data_source_folder_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_extract_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_extract_data_source").exists()

@pytest.mark.parametrize("option", ["--extract", "-e"])
def test_extract_source_files_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_extract_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_extract_data_source/metadata.md").exists()

@pytest.mark.parametrize("option", ["--extract", "-e"])
def test_extract_source_files_placeholders_replaced(create_root, option):
    result = runner.invoke(app, ["data-source", "test_extract_data_source", option])

    assert result.exit_code == 0
    with open("./data_sources/test_extract_data_source/metadata.md", "r") as md:
        md_contents = md.read()
        assert "<-project_name->" not in md_contents
        assert "# test_extract_data_source metadata" in md_contents

@pytest.mark.parametrize("option", ["--extract", "-e"])
def test_add_data_source_extract_output_printed(create_root, option):
    result = runner.invoke(app, ["data-source", "test_extract_data_source", option])

    expected_output = """
🖿 data_sources
├── 🖿 test_extract_data_sources
└── 🗋 metadata.md
    """ 
    expected_output in result.stdout

## ############ ##
## Web Download ##
## ############ ##
@pytest.mark.parametrize("option", ["--web-download", "-w"])
def test_add_web_download_data_source_folder_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_web_download_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_web_download_data_source").exists()

@pytest.mark.parametrize("option", ["--web-download", "-w"])
def test_extract_source_files_created(create_root, option):
    result = runner.invoke(app, ["data-source", "test_web_download_data_source", option])

    assert result.exit_code == 0
    assert pathlib.Path("./data_sources/test_web_download_data_source/metadata.md").exists()

@pytest.mark.parametrize("option", ["--web-download", "-w"])
def test_extract_source_files_placeholders_replaced(create_root, option):
    result = runner.invoke(app, ["data-source", "test_web_download_data_source", option])

    assert result.exit_code == 0
    with open("./data_sources/test_web_download_data_source/metadata.md", "r") as md:
        md_contents = md.read()
        assert "<-project_name->" not in md_contents
        assert "# test_web_download_data_source metadata" in md_contents

@pytest.mark.parametrize("option", ["--web-download", "-w"])
def test_add_data_source_no_web_download_output_printed(create_root, option):
    result = runner.invoke(app, ["data-source", "test_web_download_data_source", option])

    expected_output = """
🖿 data_sources
├── 🖿 test_web_download_data_sources
└── 🗋 metadata.md
    """ 
    expected_output in result.stdout
