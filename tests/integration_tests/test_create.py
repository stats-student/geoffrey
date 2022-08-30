import os
import pathlib
import pytest

from typer.testing import CliRunner

from geoffrey.main import app


runner = CliRunner()


def test_creates_project_dir(tmp_path):
    os.chdir(tmp_path)

    result = runner.invoke(app, ["create", "test_project"])

    assert result.exit_code == 0
    assert (tmp_path / "test_project").exists()
    assert "\U0001F680 test_project created!" in result.stdout


def test_creates_project_dir_path_passed(tmp_path):
    os.chdir(tmp_path)

    result = runner.invoke(app, ["create", "dev/projects/test_project", "--parents"])

    assert result.exit_code == 0
    assert (tmp_path / "dev/projects/test_project").exists()
    assert "\U0001F680 test_project created!" in result.stdout


def test_creates_subdirectories(tmp_path):
    os.chdir(tmp_path)

    result = runner.invoke(app, ["create", "test_project"])

    expected_dirs = sorted(["data_sources", "explorations", "models", "products"])
    actual_dirs = sorted(
        [i.name for i in pathlib.Path("./test_project").iterdir() if i.is_dir()]
    )

    assert result.exit_code == 0
    assert expected_dirs == actual_dirs


def test_creates_files(tmp_path):
    os.chdir(tmp_path)

    result = runner.invoke(app, ["create", "test_project"])

    expected_dirs = sorted(["README.md", "project_scoping.md", ".geoff"])
    actual_dirs = sorted(
        [i.name for i in pathlib.Path("./test_project").iterdir() if i.is_file()]
    )

    assert result.exit_code == 0
    assert expected_dirs == actual_dirs


def test_tree_is_displayed(tmp_path):
    os.chdir(tmp_path)

    result = runner.invoke(app, ["create", "test_project"])

    expected_out = """test_project
├── 🖿 data_sources
├── 🖿 explorations
├── 🖿 models
├── 🖿 products
├── 🗋 README.md
└── 🗋 project_scoping.md"""

    assert result.exit_code == 0
    assert expected_out in result.stdout
