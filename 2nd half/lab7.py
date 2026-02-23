def find_max_subarray(arr: list) -> tuple[int, int, int]:
    if not arr:
        raise ValueError("Массив пуст")

    best_sum = arr[0]
    best_l = best_r = 0

    cur_sum = arr[0]
    cur_l = 0

    for i in range(1, len(arr)):
        if cur_sum + arr[i] < arr[i]:
            cur_sum = arr[i]
            cur_l = i

        else:
            cur_sum += arr[i]

        if cur_sum > best_sum:
            best_sum = cur_sum
            best_l, best_r = cur_l, i

    return best_sum, best_l, best_r


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
best_sum, best_l, best_r = find_max_subarray(arr)

print(f"max_sum = {best_sum}")
print(f"subarray = {arr[best_l:best_r + 1]} slice = {(best_l, best_r)}")
