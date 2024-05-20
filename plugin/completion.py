from __future__ import annotations

from functools import lru_cache
from itertools import groupby
from typing import Generator, Iterable

import sublime

from .constant import DB_DIR
from .data_types import DbItem, DbModel, NormalizedDbItem
from .utils import sort_uniq


def load_db(version: str) -> DbModel:
    return DbModel.model_validate_json(sublime.load_binary_resource(str(DB_DIR / f"{version}.json")))


def get_completion_list(versions: str | tuple[str, ...]) -> sublime.CompletionList:
    """Gets the completion items."""
    # normalize `versions` for `lru_cache`
    if isinstance(versions, str):
        versions = (versions,)
    versions = tuple(sort_uniq(versions))
    return _get_completion_list(versions)


@lru_cache(maxsize=5)
def _get_completion_list(versions: tuple[str, ...]) -> sublime.CompletionList:
    """Gets the completion items. (LRU cache)"""
    db_items = [item for version in versions for item in _list_db_items(version)]

    return sublime.CompletionList(
        tuple(
            sublime.CompletionItem(
                trigger=item.item_name,
                annotation=f"{item.lib_name} {'/'.join(item.lib_versions)}",
                completion=item.item_name,
                completion_format=sublime.COMPLETION_FORMAT_TEXT,
                kind=(sublime.KIND_ID_MARKUP, "c", ""),
                details="",
            )
            for item in _normalize_db_items_for_completion(db_items)
        )
    )


def _list_db_items(version: str) -> Generator[DbItem, None, None]:
    db = load_db(version)
    yield from (DbItem(lib_name=db.name, lib_version=db.version, item_name=name) for name in db.classes)


def _normalize_db_items_for_completion(db_items: Iterable[DbItem]) -> Generator[NormalizedDbItem, None, None]:
    def sorter(item: DbItem) -> tuple[str, str]:
        return (item.lib_name, item.item_name)

    # pre-sort for groupby
    db_items = sorted(db_items, key=sorter)
    # merges same-name items which have different versions
    for (lib_name, item_name), group in groupby(db_items, sorter):
        yield NormalizedDbItem(
            lib_name=lib_name,
            lib_versions=sorted(item.lib_version for item in group),
            item_name=item_name,
        )
