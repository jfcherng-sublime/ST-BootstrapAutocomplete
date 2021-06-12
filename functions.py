from .consts import COMPLETION_DB_FILE
from .consts import PACKAGE_NAME
from .consts import SETTINGS_FILENAME
from dataclasses import dataclass
from functools import lru_cache
from itertools import groupby
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple
import sublime


@dataclass
class DatabaseItem:
    version: str
    name: str


@dataclass
class NormalizedDatabaseItem:
    versions: Sequence[str]
    name: str


def get_plugin_setting(key: str, default: Optional[Any] = None) -> Any:
    return get_plugin_settings().get(key, default)


def get_plugin_settings() -> sublime.Settings:
    project_data = sublime.active_window().project_data() or {}
    project_settings = project_data.get("settings", {})  # type: Dict[str, Any]

    settings = sublime.load_settings(SETTINGS_FILENAME)
    settings.update(project_settings.get(PACKAGE_NAME, {}))

    return settings


@lru_cache
def get_completion_items(version_str: str) -> List[sublime.CompletionItem]:
    """
    Gets the completion items.

    :param      version_str:  Versions separated with ","
    :type       version_str:  str

    :returns:   The completion items.
    :rtype:     List[sublime.CompletionItem]
    """

    versions = set(version_str.split(",") if version_str else [])

    items = get_database_items()
    items = filter(lambda item: item.version in versions, items)

    return list(
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
        ),
    )


@lru_cache
def get_database_items() -> Tuple[DatabaseItem, ...]:
    return tuple(
        map(
            lambda item: DatabaseItem(*item),
            sublime.decode_value(sublime.load_resource(COMPLETION_DB_FILE)),
        )
    )


def normalize_database_items(items: Iterable[DatabaseItem]) -> Iterator[NormalizedDatabaseItem]:
    # pre-sort for groupby
    items = sorted(items, key=lambda item: item.name)

    # merges same-name items which have different versions
    for name, group in groupby(items, lambda item: item.name):
        yield NormalizedDatabaseItem(sorted(item.version for item in group), name)
