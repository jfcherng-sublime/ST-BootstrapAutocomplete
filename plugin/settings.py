from .constant import PLUGIN_NAME
from .constant import SETTINGS_FILENAME
from typing import Any, Dict, Optional, Tuple
import sublime


def get_plugin_setting(window: sublime.Window, key: str, default: Optional[Any] = None) -> Any:
    return get_plugin_settings(window).get(key, default)


def get_plugin_settings(window: sublime.Window) -> Dict[str, Any]:
    project_plugin_settings: Dict[str, Any] = (window.project_data() or {}).get("settings", {}).get(PLUGIN_NAME, {})

    settings = sublime.load_settings(SETTINGS_FILENAME).to_dict()
    settings.update(project_plugin_settings)

    return settings


def get_versions(window: sublime.Window) -> Tuple[str, ...]:
    versions = get_plugin_setting(window, "versions", [])
    if not isinstance(versions, list):
        versions = [versions]
    return tuple(map(str, versions))  # in case someone uses int values...


def get_selectors(window: sublime.Window) -> Tuple[str, ...]:
    selectors = get_plugin_setting(window, "selectors", [])
    if not isinstance(selectors, list):
        selectors = [selectors]
    return tuple(selectors)
