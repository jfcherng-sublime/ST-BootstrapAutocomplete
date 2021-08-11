from typing import Generator, Iterable, Optional, Set
import fire
import io
import json
import requests
import sys
import tinycss2
import tinycss2.ast

# always use \n as line ending for printing
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, newline="\n")


def extract_stylesheet_class_names(
    path: str,
    output_format: str = "json",
    lib_name: str = "UnknownLib",
    lib_version: str = "0",
) -> None:
    """
    Extract class names from the stylesheet.

    :param      path:           The path or URL of the stylesheet
    :type       path:           str
    :param      output_format:  The output format
    :type       output_format:  str
    :param      lib_name:       The library name
    :type       lib_name:       str
    :param      lib_version:    The library version
    :type       lib_version:    str
    """
    class_names: Set[str] = set()
    content = get_file_content(path)
    rules = tinycss2.parse_stylesheet(content)

    for rule in rules:
        if isinstance(rule, tinycss2.ast.AtRule):
            if not rule.content:
                continue
            class_names |= set(find_class_names(rule.content))
            continue

        if isinstance(rule, tinycss2.ast.QualifiedRule):
            class_names |= set(find_class_names(rule.prelude))
            continue

    class_names_sorted = sorted(class_names)

    if output_format == "json":
        print(
            json.dumps(
                {
                    "name": lib_name,
                    "version": str(lib_version),
                    "classes": class_names_sorted,
                },
                ensure_ascii=False,
                indent="\t",
            )
        )
    else:
        print("\n".join(class_names_sorted))


def find_class_names(nodes: Iterable[tinycss2.ast.Node]) -> Generator[str, None, None]:
    prev_node: Optional[tinycss2.ast.Node] = None
    for node in nodes:
        if (
            isinstance(prev_node, tinycss2.ast.LiteralToken)
            and prev_node.value == "."
            and isinstance(node, tinycss2.ast.IdentToken)
        ):
            yield node.value
        prev_node = node


def get_file_content(path: str) -> str:
    """
    Gets the file content.

    :param      path:  The path or URL of file
    :type       path:  str

    :returns:   The file content.
    :rtype:     str
    """
    if path.startswith(("http://", "https://")):
        return str(requests.get(path).content, "utf-8")

    with io.open(path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    fire.Fire(extract_stylesheet_class_names)
