from __future__ import annotations

from pydantic import BaseModel


class DbModel(BaseModel):
    name: str
    version: str
    classes: list[str]


class DbItem(BaseModel):
    lib_name: str
    """The name of the lib."""
    lib_version: str
    """The version of the lib."""
    item_name: str
    """The trigger of the completion."""


class NormalizedDbItem(BaseModel):
    lib_name: str
    """The name of the lib."""
    lib_versions: list[str]
    """Versions of the lib."""
    item_name: str
    """The trigger of the completion."""
