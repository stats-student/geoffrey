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
