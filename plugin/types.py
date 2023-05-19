from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class DbSchema(TypedDict):
    name: str
    version: str
    classes: list[str]


@dataclass
class DatabaseItem:
    lib_name: str  # the name of the lib
    lib_version: str  # the version of the lib
    item_name: str  # the trigger of the completion


@dataclass
class NormalizedDatabaseItem:
    lib_name: str  # the name of the lib
    lib_versions: tuple[str, ...]  # versions of the lib
    item_name: str  # the trigger of the completion
