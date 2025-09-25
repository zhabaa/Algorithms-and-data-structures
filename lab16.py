"""
lab16_iterative_preorder.py

Нерекурсивный прямой обход (preorder) с использованием явного стека.
"""

from tree_parser import parse_linear


def preorder_iter(root, visit):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        visit(node.key)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


def main():
    s = input().strip()

    root = parse_linear(s)

    if root is None:
        raise Exception("Cant parse tree")

    res = []
    preorder_iter(root, lambda k: res.append(str(k)))
    print("Iterative Preorder:", " ".join(res))


if __name__ == "__main__":
    main()
