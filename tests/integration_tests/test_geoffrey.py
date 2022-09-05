import os
import pathlib
import pytest
import subprocess

from typer.testing import CliRunner

from geoffrey.main import app


runner = CliRunner()


def test_command_exists(tmp_path):
    os.chdir(tmp_path)

    result = runner.invoke(app, ["create", "--help"])
    assert result.exit_code == 0


def test_sub_command_exists():
    result = runner.invoke(app, ["add", "--help"])
    assert result.exit_code == 0


@pytest.mark.parametrize(
    "add_command", ["data-source", "exploration", "model", "product"]
)
def test_add_non_geoff_directory(create_root, add_command):
    os.chdir("..")

    result = runner.invoke(app, ["add", add_command, "test_" + add_command])

    assert result.exc_info[0] == RuntimeError
    assert str(result.exc_info[1]) == (
        "This directory isn't managed by geoff. Please change to a directory that is"
    )
