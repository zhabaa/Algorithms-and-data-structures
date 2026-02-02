from dataclasses import dataclass
from typing import Optional, Self


@dataclass
class Node:
    key: int
    left: Self | None = None
    right: Self | None = None


def parse_linear(s: str) -> Optional[Node]:
    if not s:
        return None

    s = "".join(s.split())

    def parse_subtree(start: int) -> tuple[Optional[Node], int]:
        if start >= len(s) or s[start] in ",)":
            return None, start

        end = start

        if s[end] in "+-":
            end += 1

        while end < len(s) and s[end].isdigit():
            end += 1

        if end == start or (s[start] in "+-" and end == start + 1):
            return None, start

        node = Node(int(s[start:end]))
        pos = end

        if pos < len(s) and s[pos] == "(":
            node.left, pos = parse_subtree(pos + 1)  # после '('

            if pos < len(s) and s[pos] == ",":
                node.right, pos = parse_subtree(pos + 1)  # после ','

            if pos < len(s) and s[pos] == ")":
                pos += 1

        return node, pos

    root, _ = parse_subtree(0)
    return root


def print_linear(root: Optional[Node]) -> str:
    if not root:
        return ""

    result = str(root.key)

    if root.left or root.right:
        result += f"({print_linear(root.left)},{print_linear(root.right)})"

    return result
