import filecmp
import os
import pathlib
import pytest

from rich.tree import Tree

from geoffrey.add_commands import _add_data_source_command

## #################### ##
## AddDataSourceCommand ##
## #################### ##
def test_add_data_source_command_exists():
    assert "AddCommand" in dir(_add_data_source_command)
    assert callable(_add_data_source_command.AddDataSourceCommand)

## ############## ##
## copy_templates ##
## ############## ##
@pytest.mark.parametrize(
    "template",
    ["db_metadata.md", "empty_metadata.md", "extract_metadata.md", "web_metadata.md"]
)
def test_template_copied(create_root, template):
    ads = _add_data_source_command.AddDataSourceCommand("test_data_source")
    ads.create_dir()

    ads.copy_templates(template)

    assert pathlib.Path(f"data_sources/test_data_source/metadata.md").exists()
    assert filecmp.cmp(str(ads.metadata_template), "data_sources/test_data_source/metadata.md")

## #################### ##
## replace_placeholders ##
## #################### ##
@pytest.mark.parametrize(
    "template",
    ["db_metadata.md", "empty_metadata.md", "extract_metadata.md", "web_metadata.md"]
)
def test_placeholder_tags_replaced(create_root, template):
    ads = _add_data_source_command.AddDataSourceCommand("test_data_source")
    ads.create_dir()
    ads.copy_templates(template)

    ads.replace_placeholders()

    with open("./data_sources/test_data_source/metadata.md", "r") as md:
        md_contents = md.read()
        assert "<-project_name->" not in md_contents
        assert "# test_data_source metadata" in md_contents

## ########### ##
## create_tree ##
## ########### ##
def test_tree_printed(create_root, capsys):
    ads = _add_data_source_command.AddDataSourceCommand("test_data_source")
    tree = ads.create_tree()

    expected_tree = Tree("[gold1]\U0001F5BF [bold dodger_blue2]data_sources")
    expected_tree_ds = expected_tree.add(f"[gold1]\U0001F5BF [bold dodger_blue2]test_data_source")
    expected_tree_ds.add("[honeydew2]\U0001F5CB [spring_green2]metadata.md")

    expected_leaves = sorted([leaf.label for leaf in expected_tree_ds.children])

    actual_leaves = sorted([leaf.label for leaf in tree.children])

    assert expected_leaves == actual_leaves
