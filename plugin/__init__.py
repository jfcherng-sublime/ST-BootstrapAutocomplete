from .constant import PLUGIN_NAME

# import all listeners and commands
from .listener import BootstrapAutocompleteEventListener
from .settings import AioSettings, settings_normalizer

__all__ = (
    # ST: core
    "plugin_loaded",
    "plugin_unloaded",
    # ST: listeners
    "AioSettings",
    "BootstrapAutocompleteEventListener",
)


def plugin_loaded() -> None:
    AioSettings.plugin_name = PLUGIN_NAME
    AioSettings.set_settings_normalizer(settings_normalizer)
    AioSettings.set_up()


def plugin_unloaded() -> None:
    AioSettings.tear_down()
