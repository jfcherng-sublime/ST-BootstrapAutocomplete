from .completion import get_completion_list
from .settings import get_merged_plugin_setting
from typing import Iterable, List, Optional
import sublime
import sublime_plugin


class BootstrapAutocomplete(sublime_plugin.EventListener):
    def on_query_completions(
        self,
        view: sublime.View,
        prefix: str,
        locations: List[int],
    ) -> Optional[sublime.CompletionList]:
        if view.element() or not (window := view.window()):
            return None

        point = locations[0]
        selectors: List[str] = get_merged_plugin_setting(window, "selectors")

        if not self._point_match_selectors(view, point, selectors):
            return None

        return get_completion_list(",".join(get_merged_plugin_setting(window, "versions")))

    @staticmethod
    def _point_match_selectors(view: sublime.View, point: int, selectors: Iterable[str]) -> bool:
        return any(view.match_selector(point, selector) for selector in selectors)
