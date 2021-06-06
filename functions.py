from .consts import DB_FILE
from .consts import PACKAGE_NAME
from .consts import SETTINGS_FILENAME
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Dict, List, Optional, Tuple
import sublime


@dataclass
class DatabaseItem:
    version: str
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
    items = sorted(items, key=lambda item: (item.version, item.name))

    return list(
        map(
            lambda item: sublime.CompletionItem(
                trigger=item.name,
                annotation=f"Bootstrap {item.version}",
                completion=item.name,
                completion_format=sublime.COMPLETION_FORMAT_TEXT,
                kind=(sublime.KIND_ID_MARKUP, "c", ""),
                details="",
            ),
            items,
        ),
    )


@lru_cache
def get_database_items() -> Tuple[DatabaseItem, ...]:
    return tuple(
        map(
            lambda item: DatabaseItem(*item),
            sublime.decode_value(sublime.load_resource(DB_FILE)),
        )
    )
