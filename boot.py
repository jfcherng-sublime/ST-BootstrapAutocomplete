from .plugin import set_up
from .plugin import tear_down
from .plugin.listener import *  # noqa: F401, F403
from .plugin.settings import AioSettings  # noqa: F401


def plugin_loaded() -> None:
    set_up()


def plugin_unloaded() -> None:
    tear_down()
