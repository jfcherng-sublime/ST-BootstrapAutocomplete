from __future__ import annotations

from typing import Iterable

import sublime
import sublime_plugin

from .completion import get_completion_list
from .settings import get_merged_plugin_setting


class BootstrapAutocompleteEventListener(sublime_plugin.EventListener):
    def on_query_completions(
        self,
        view: sublime.View,
        prefix: str,
        locations: list[int],
    ) -> sublime.CompletionList | None:
        if view.element() or not (window := view.window()):
            return None

        point = locations[0]
        selectors: list[str] = get_merged_plugin_setting(window, "selectors")

        if not self._point_match_selectors(view, point, selectors):
            return None

        versions = get_merged_plugin_setting(window, "versions")
        return get_completion_list(versions)

    @staticmethod
    def _point_match_selectors(view: sublime.View, point: int, selectors: Iterable[str]) -> bool:
        return any(view.match_selector(point, selector) for selector in selectors)
