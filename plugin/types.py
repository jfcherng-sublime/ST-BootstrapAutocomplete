from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict


class DbSchema(TypedDict):
    name: str
    version: str
    classes: list[str]


@dataclass
class DatabaseItem:
    lib_name: str
    """The name of the lib."""
    lib_version: str
    """The version of the lib."""
    item_name: str
    """The trigger of the completion."""


@dataclass
class NormalizedDatabaseItem:
    lib_name: str
    """The name of the lib."""
    lib_versions: list[str]
    """Versions of the lib."""
    item_name: str
    """The trigger of the completion."""
