def shell_sort(arr) -> list[int]:
    last_index = len(arr)
    step = len(arr) // 2

    while step > 0:
        for i in range(step, last_index):
            j = i
            delta = j - step

            while delta >= 0 and arr[delta] > arr[j]:
                arr[delta], arr[j] = arr[j], arr[delta]
                j = delta
                delta = j - step

        step //= 2

    return arr
