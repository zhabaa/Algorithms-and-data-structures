"""
Comb sort
"""


def comb_sort(arr):
    lenght = len(arr)
    gap = lenght
    shrink = 1.3
    is_sorted = False

    while not is_sorted:
        gap = int(gap / shrink)

        if gap <= 1:
            is_sorted = True
            gap = 1

        for left in range(lenght - gap):
            right = left + gap

            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]

                is_sorted = False

    return arr
