from .completion import get_completion_list
from .settings import get_selectors
from .settings import get_versions
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
        if not (window := view.window()) or not self._point_match_selectors(view, locations[0], get_selectors(window)):
            return None

        return get_completion_list(",".join(get_versions(window)))

    @staticmethod
    def _point_match_selectors(view: sublime.View, point: int, selectors: Iterable[str]) -> bool:
        return any(view.match_selector(point, selector) for selector in selectors)
