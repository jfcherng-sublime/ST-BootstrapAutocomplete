from dataclasses import dataclass
from typing import List, Tuple, TypedDict


class DbSchema(TypedDict):
    name: str
    version: str
    classes: List[str]


@dataclass
class DatabaseItem:
    lib_name: str  # the name of the lib
    lib_version: str  # the version of the lib
    item_name: str  # the trigger of the completion


@dataclass
class NormalizedDatabaseItem:
    lib_name: str  # the name of the lib
    lib_versions: Tuple[str, ...]  # versions of the lib
    item_name: str  # the trigger of the completion
