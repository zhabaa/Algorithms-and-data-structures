"""
Radix sort
"""


def radix_sort(arr, base=10):
    max_digits = max([len(str(x)) for x in arr])
    bins = [[] for _ in range(base)]

    for i in range(0, max_digits):
        for x in arr:
            digit = (x // base ** i) % base
            bins[digit].append(x)

        arr = list()

        for queue in bins:
            for x in queue:
                arr.append(x)

        bins = [[] for _ in range(base)]

    return arr
