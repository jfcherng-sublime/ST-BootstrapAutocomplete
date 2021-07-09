from .constant import PACKAGE_NAME
from .constant import SETTINGS_FILENAME
from typing import Any, Dict, Optional
import sublime


def get_plugin_setting(key: str, default: Optional[Any] = None) -> Any:
    return get_plugin_settings().get(key, default)


def get_plugin_settings() -> sublime.Settings:
    project_data = sublime.active_window().project_data() or {}
    project_settings: Dict[str, Any] = project_data.get("settings", {})
    project_plugin_settings: Dict[str, Any] = project_settings.get(PACKAGE_NAME, {})

    settings = sublime.load_settings(SETTINGS_FILENAME)
    settings.update(project_plugin_settings)

    return settings
