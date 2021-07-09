from .completion import get_completion_items
from .settings import get_plugin_setting
from typing import Iterable, List
import sublime
import sublime_plugin


class BootstrapAutocomplete(sublime_plugin.EventListener):
    def on_query_completions(
        self,
        view: sublime.View,
        prefix: str,
        locations: List[int],
    ) -> List[sublime.CompletionItem]:
        point = locations[0]
        selectors: List[str] = get_plugin_setting("selectors")

        if self._point_match_selectors(view, point, selectors):
            return self._get_completion_items()

        return []

    @staticmethod
    def _point_match_selectors(view: sublime.View, point: int, selectors: Iterable[str]) -> bool:
        return any(view.match_selector(point, selector) for selector in selectors)

    @staticmethod
    def _get_completion_items() -> List[sublime.CompletionItem]:
        # in case someone uses int values...
        versions = map(str, get_plugin_setting("versions"))

        return get_completion_items(",".join(versions))
