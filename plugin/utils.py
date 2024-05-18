from __future__ import annotations

from itertools import groupby
from operator import itemgetter
from typing import Any, Callable, Generator, Iterable, TypeVar

_T = TypeVar("_T")


def sort_uniq(
    seq: Iterable[_T],
    *,
    key: Callable[[_T], Any] | None = None,
    reverse: bool = False,
) -> Generator[_T, None, None]:
    key = key or (lambda x: x)
    yield from map(
        itemgetter(0),
        groupby(sorted(seq, key=key, reverse=reverse), key=key),  # type: ignore
    )
