import re


def read_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()

    words = re.findall(r"[a-zа-я0-9]+", text)
    return words


def hash_func(word, size):
    return sum(ord(c) for c in word) % size


def hash_table_open_addressing(words, size=20):
    table = [None] * size

    for word in words:
        idx = hash_func(word, size)
        start = idx

        while table[idx] is not None and table[idx] != word:
            idx = (idx + 1) % size

            if idx == start:
                raise Exception("Table overflow")

        table[idx] = word

    return table


def save_table(filename, table):
    with open(filename, "w", encoding="utf-8") as f:
        for i, val in enumerate(table):
            f.write(f"{i}: {val}\n")


if __name__ == "__main__":
    words = read_words("lab13-14/input1.txt")
    table = hash_table_open_addressing(words, size=20)
    save_table("output.txt", table)
