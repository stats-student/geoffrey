import os
import pathlib
import pytest

from geoffrey.add_commands import _add_base_command

## ########## ##
## AddCommand ##
## ########## ##
def test_base_add_command_exists():
    assert "AddCommand" in dir(_add_base_command)
    assert callable(_add_base_command.AddCommand)

## ######################## ##
## _check_dir_name_is_valid ##
## ######################## ##
def test_empty_name(create_root):
    ads = _add_base_command.AddCommand(
            "data_sources",
            "placeholder_name"
        )

    expected_msg = (
        "You passed an empty string as the data source name. Please pass a valid name"
    )

    with pytest.raises(ValueError) as excinfo:
        ads._check_dir_name_is_valid("")

    assert str(excinfo.value) == expected_msg

## ################### ##
## check_is_geoff_dir ##
## ################### ##
def test_check_if_geoff_dir_is_true(create_root):
    ads = _add_base_command.AddCommand(
        "data_sources",
        "test_data_source"
    )

    assert ads.check_is_geoff_dir()

def test_check_if_geoff_dir_is_false(create_root):
    os.chdir("..")
    ads = _add_base_command.AddCommand(
        "data_sources",
        "test_data_source"
    )

    assert not ads.check_is_geoff_dir()

## ########## ##
## create_dir ##
## ########## ##
def test_create_data_source_directory(create_root):
    ads = _add_base_command.AddCommand(
        "data_sources",
        "test_data_source"
    )

    ads.create_dir()

    assert pathlib.Path("./data_sources/test_data_source").exists()

def test_create_dir_empty_name(create_root):
    expected_msg = (
        "You passed an empty string as the data source name. Please pass a valid name"
    )

    with pytest.raises(ValueError) as excinfo:
        ads = _add_base_command.AddCommand(
            "data_sources",
            ""
        )

    assert str(excinfo.value) == expected_msg
