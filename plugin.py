from .functions import get_completion_items
from .functions import get_plugin_setting
from typing import List
import sublime
import sublime_plugin


class BootstrapAutocomplete(sublime_plugin.EventListener):
    def on_query_completions(
        self, view: sublime.View, prefix: str, locations: List[int]
    ) -> List[sublime.CompletionItem]:
        point = locations[0]
        selector = self._get_normalized_selector()

        if selector and view.match_selector(point, selector):
            return self._get_completion_items()

        if view.match_selector(point, "text.html string.quoted"):
            limit = 250
            cursor = point - len(prefix) - 1
            start = max(0, cursor - limit - len(prefix))
            line = view.substr(sublime.Region(start, cursor))
            parts = line.split("=")

            if len(parts) > 1 and parts[-2].strip().endswith("class"):
                return self._get_completion_items()

        return []

    @staticmethod
    def _get_normalized_selector() -> str:
        selectors = get_plugin_setting("selectors")  # type: List[str]

        return "(" + ")|(".join(selectors) + ")" if selectors else ""

    @staticmethod
    def _get_completion_items() -> List[sublime.CompletionItem]:
        # in case someone uses int values...
        versions = map(str, get_plugin_setting("versions"))

        return get_completion_items(",".join(versions))
