import pathlib

from typing import List, Optional

class AddCommand:

    def __init__(
        self,
        command: str,
        name: str
    ) -> None:
        self.command = command
        self.name = self._check_dir_name_is_valid(name)

    def _check_dir_name_is_valid(self, name: str) -> str:
        if name == "":
            raise ValueError(
                "You passed an empty string as the data source name. Please pass a valid name"
            )
        else:
            return name
    
    def check_is_geoff_dir(self) -> bool:
        return pathlib.Path(".geoff").exists()
    
    def create_dir(self) -> None:
        pathlib.Path(f"{self.command}/{self.name}").mkdir(parents=False)
