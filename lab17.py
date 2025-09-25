from tree_parser import parse_linear, print_linear


def bst_search(root, key):
    cur = root

    while cur:
        if key == cur.key:
            return cur

        elif key < cur.key:
            cur = cur.left

        else:
            cur = cur.right

    return None


def bst_insert(root, key):
    if root is None:
        return type(root)(key)

    parent = None
    cur = root

    while cur:
        parent = cur

        if key == cur.key:
            return root

        elif key < cur.key:
            cur = cur.left

        else:
            cur = cur.right

    if key < parent.key:
        parent.left = type(parent)(key)

    else:
        parent.right = type(parent)(key)

    return root


def find_min(node):
    cur = node

    while cur and cur.left:
        cur = cur.left

    return cur


def bst_delete(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = bst_delete(root.left, key)

    elif key > root.key:
        root.right = bst_delete(root.right, key)

    else:
        if root.left is None and root.right is None:
            return None

        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        succ = find_min(root.right)
        root.key = succ.key
        root.right = bst_delete(root.right, succ.key)

    return root


def read_int(prompt=""):
    try:
        return int(input(prompt))

    except Exception as ex:
        raise Exception(f"Некорректный ввод. {ex}")


def main():
    s = input().strip()
    root = parse_linear(s)

    if root is None:
        raise Exception("Cant parse tree")

    while True:
        print(
            "\nМеню:",
            "1 - search node",
            "2 - insert node",
            "3 - delete node",
            "4 - show tree",
            "0 - exit",
            sep="\n",
        )
        cmd = input("Select option: ").strip()

        match cmd:
            case "0":
                break

            case "1":
                key = read_int("Key for search: ")

                if key is None:
                    continue

                found = bst_search(root, key)
                print("\nFound" if found else "Not found")

            case "2":
                key = read_int("Key for insert: ")

                if key is None:
                    continue

                if root is None:
                    root = type(parse_linear("1"))(key)

                    from tree_parser import Node

                    root = Node(key)
                    print("\nInserted as root")
                    continue

                root = bst_insert(root, key)
                print("\nInserted")

            case "3":
                key = read_int("Key to delete: ")

                if key is None:
                    continue

                root = bst_delete(root, key)
                print("\nKey deleted")

            case "4":
                print(f"\nTree: {print_linear(root)}")

            case _:
                print("\nUnsupported operation")


if __name__ == "__main__":
    main()
