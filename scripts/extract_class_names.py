from __future__ import annotations

import gzip
import io
import json
import sys
import urllib.request
from collections.abc import Generator, Iterable
from enum import StrEnum
from pathlib import Path
from typing import Annotated

import tinycss2.ast as cssast
import typer
from tinycss2 import parse_stylesheet

# always use \n as line ending for printing
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, newline="\n")


class CliOutputFormat(StrEnum):
    JSON = "json"
    TEXT = "text"


app = typer.Typer(add_completion=False)


@app.command()
def extract_stylesheet_class_names(
    path: Annotated[str, typer.Argument(help="The path or URL of the stylesheet.")],
    output_format: Annotated[CliOutputFormat, typer.Option(help="The output format.")] = CliOutputFormat.JSON,
    lib_name: Annotated[str, typer.Option(help="The library name.")] = "Untitled",
    lib_version: Annotated[str, typer.Option(help="The library version.")] = "0",
) -> None:
    """Extract class names from the stylesheet."""
    if path.startswith(("http://", "https://")):
        content = str(simple_urlopen(path), "utf-8")
    else:
        content = Path(path).read_text(encoding="utf-8")

    class_names: set[str] = set()
    rules = parse_stylesheet(content)
    for rule in rules:
        if isinstance(rule, cssast.AtRule) and rule.content:
            class_names |= set(find_class_names(rule.content))
            continue
        if isinstance(rule, cssast.QualifiedRule):
            class_names |= set(find_class_names(rule.prelude))
            continue

    class_names_sorted = sorted(class_names)

    if output_format is CliOutputFormat.JSON:
        print(
            json.dumps(
                {
                    "name": lib_name,
                    "version": lib_version,
                    "classes": class_names_sorted,
                },
                ensure_ascii=False,
                indent="\t",
            )
        )
    else:
        print("\n".join(class_names_sorted))


def find_class_names(nodes: Iterable[cssast.Node]) -> Generator[str]:
    prev_node: cssast.Node | None = None
    for node in nodes:
        if (
            isinstance(prev_node, cssast.LiteralToken)
            and prev_node.value == "."
            and isinstance(node, cssast.IdentToken)
        ):
            yield node.value
        prev_node = node


def simple_urlopen(url: str, *, chunk_size: int = 512 * 1024) -> bytes:
    with urllib.request.urlopen(url) as resp:
        data = b""
        while chunk := resp.read(chunk_size):
            data += chunk
        if resp.info().get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
    return data


if __name__ == "__main__":
    app()
