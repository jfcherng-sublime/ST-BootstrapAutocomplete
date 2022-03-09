from .constant import DB_DIR
from .types import DatabaseItem, DbSchema, NormalizedDatabaseItem
from functools import lru_cache
from itertools import groupby
from typing import Generator, Iterable, Tuple
import sublime


@lru_cache
def load_database(version: str) -> DbSchema:
    return sublime.decode_value(sublime.load_resource(str(DB_DIR / f"{version}.json")))


@lru_cache
def get_completion_list(version_str: str) -> sublime.CompletionList:
    """
    Gets the completion items.

    :param      version_str:  Versions separated with ","
    :type       version_str:  str

    :returns:   The completion items.
    :rtype:     sublime.CompletionList
    """

    versions = tuple(sorted(set(version_str.split(",") if version_str else [])))
    items = _get_database_items(versions)

    return sublime.CompletionList(
        tuple(
            map(
                lambda item: sublime.CompletionItem(
                    trigger=item.item_name,
                    annotation=f"{item.lib_name} {'/'.join(item.lib_versions)}",
                    completion=item.item_name,
                    completion_format=sublime.COMPLETION_FORMAT_TEXT,
                    kind=(sublime.KIND_ID_MARKUP, "c", ""),
                    details="",
                ),
                _normalize_database_items(items),
            )
        )
    )


def _get_database_items(versions: Iterable[str]) -> Generator[DatabaseItem, None, None]:
    for version in versions:
        db = load_database(version)
        for name in db["classes"]:
            yield DatabaseItem(
                lib_name=db["name"],
                lib_version=db["version"],
                item_name=name,
            )


def _normalize_database_items(items: Iterable[DatabaseItem]) -> Generator[NormalizedDatabaseItem, None, None]:
    def sorter(item: DatabaseItem) -> Tuple[str, str]:
        return (item.lib_name, item.item_name)

    # pre-sort for groupby
    items = sorted(items, key=sorter)

    # merges same-name items which have different versions
    for _, group in groupby(items, sorter):
        group_items = tuple(group)
        group_item = group_items[0]
        yield NormalizedDatabaseItem(
            lib_name=group_item.lib_name,
            lib_versions=tuple(sorted(item.lib_version for item in group_items)),
            item_name=group_item.item_name,
        )
