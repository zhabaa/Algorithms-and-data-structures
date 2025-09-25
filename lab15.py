"""
lab15_recursive.py

Рекурсивные обходы: прямой (preorder), центральный (inorder), концевой (postorder).
Использует tree_utils.parse_linear для чтения дерева.
"""

from tree_parser import parse_linear


def preorder(root, visit):
    if root is None:
        return

    visit(root.key)

    preorder(root.left, visit)
    preorder(root.right, visit)


def inorder(root, visit):
    if root is None:
        return

    inorder(root.left, visit)
    
    visit(root.key)
    
    inorder(root.right, visit)


def postorder(root, visit):
    if root is None:
        return
    
    postorder(root.left, visit)
    postorder(root.right, visit)
    
    visit(root.key)


def main():
    print("Enter tree in linear parenthesis sequence:")
    
    s = input().strip()
    root = parse_linear(s)

    if root is None:
        raise Exception("Cant parse tree")

    res = []
    preorder(root, lambda k: res.append(str(k)))
    print("Preorder:", " ".join(res))

    res = []
    inorder(root, lambda k: res.append(str(k)))
    print("Inorder:", " ".join(res))

    res = []
    postorder(root, lambda k: res.append(str(k)))
    print("Postorder:", " ".join(res))


if __name__ == "__main__":
    main()
