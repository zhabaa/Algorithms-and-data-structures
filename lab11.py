"""
Quick sort
"""

import random


def quick_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr
    elif n == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    sup = random.randint(0, n - 1)
    left = []
    mid = []
    right = []

    for i in range(n):
        if arr[i] < arr[sup]:
            left.append(arr[i])
        elif arr[i] == arr[sup]:
            mid.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + mid + quick_sort(right)
