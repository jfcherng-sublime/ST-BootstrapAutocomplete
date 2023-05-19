from __future__ import annotations

from pathlib import Path

PLUGIN_NAME = __package__.partition(".")[0]
DB_DIR = Path(f"Packages/{PLUGIN_NAME}/db")
