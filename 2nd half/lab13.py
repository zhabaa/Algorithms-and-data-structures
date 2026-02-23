def bin_packing(weights: list[int], bin_capacity: int) -> tuple[int, list[list[int]]]:
    bins: list[list[int]] = []
    
    for weight in weights:
        placed = False

        for b in bins:
            if sum(b) + weight <= bin_capacity:
                b.append(weight)
                placed = True
                break

        if not placed:
            bins.append([weight])
    
    return len(bins), bins


weights = [4, 8, 1, 4, 3, 6]
bin_capacity = 10

print(bin_packing(weights, bin_capacity))
