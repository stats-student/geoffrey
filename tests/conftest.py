import os
import pytest


@pytest.fixture()
def create_root(tmp_path):
    os.chdir(tmp_path)

    for folder in ["data_sources", "explorations", "models", "products"]:
        os.mkdir(folder)

    for file in ["README.md", "project_scoping.md", ".geoff"]:
        open(file, "a").close()

    yield
