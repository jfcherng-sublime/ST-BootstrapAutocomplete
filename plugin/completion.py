from .constant import COMPLETION_DB_PATH
from dataclasses import dataclass
from functools import lru_cache
from itertools import groupby
from typing import Generator, Iterable, Sequence, Tuple
import sublime


@dataclass
class DatabaseItem:
    version: str
    name: str


@dataclass
class NormalizedDatabaseItem:
    versions: Sequence[str]
    name: str


@lru_cache
def get_completion_list(version_str: str) -> sublime.CompletionList:
    """
    Gets the completion items.

    :param      version_str:  Versions separated with ","
    :type       version_str:  str

    :returns:   The completion items.
    :rtype:     sublime.CompletionList
    """

    versions = set(version_str.split(",") if version_str else [])

    items: Iterable[DatabaseItem] = get_database_items()
    items = filter(lambda item: item.version in versions, items)

    return sublime.CompletionList(
        tuple(
            map(
                lambda item: sublime.CompletionItem(
                    trigger=item.name,
                    annotation=f"Bootstrap {'/'.join(item.versions)}",
                    completion=item.name,
                    completion_format=sublime.COMPLETION_FORMAT_TEXT,
                    kind=(sublime.KIND_ID_MARKUP, "c", ""),
                    details="",
                ),
                normalize_database_items(items),
            )
        )
    )


@lru_cache
def get_database_items() -> Tuple[DatabaseItem, ...]:
    return tuple(
        map(
            lambda item: DatabaseItem(*item),
            sublime.decode_value(sublime.load_resource(COMPLETION_DB_PATH)),
        )
    )


def normalize_database_items(items: Iterable[DatabaseItem]) -> Generator[NormalizedDatabaseItem, None, None]:
    def sorter(item: DatabaseItem) -> str:
        return item.name

    # pre-sort for groupby
    items = sorted(items, key=sorter)

    # merges same-name items which have different versions
    for name, group in groupby(items, sorter):
        yield NormalizedDatabaseItem(sorted(item.version for item in group), name)
