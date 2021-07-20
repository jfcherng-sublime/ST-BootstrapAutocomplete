from .constant import PLUGIN_NAME
from .settings import AioSettings
from .settings import settings_normalizer


def set_up() -> None:
    AioSettings.plugin_name = PLUGIN_NAME
    AioSettings.set_settings_normalizer(settings_normalizer)
    AioSettings.set_up()


def tear_down() -> None:
    AioSettings.tear_down()
