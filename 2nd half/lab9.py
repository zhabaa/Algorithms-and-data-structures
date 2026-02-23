INFINITY = 10 ** 9


def solve(distance: list) -> tuple[int, list]:
    n = len(distance)
    
    dp = [[INFINITY] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    dp[1][0] = 0

    for mask in range(1 << n):

        for i in range(n):
            if not (mask >> i) & 1 or dp[mask][i] == INFINITY:
                continue

            for j in range(n):
                if (mask >> j) & 1:
                    continue

                new_mask = mask | (1 << j)
                new_cost = dp[mask][i] + distance[i][j]

                if new_cost < dp[new_mask][j]:
                    dp[new_mask][j] = new_cost
                    parent[new_mask][j] = i

    full_mask = (1 << n) - 1
    best_cost = INFINITY
    last_city = -1

    for i in range(1, n):
        if dp[full_mask][i] == INFINITY:
            continue
        
        total = dp[full_mask][i] + distance[i][0]

        if total < best_cost:
            best_cost = total
            last_city = i

    if best_cost == INFINITY:
        return -1, []

    path = list()
    mask = full_mask
    city = last_city

    while city != -1:
        path.append(city)
        p = parent[mask][city]
        mask = mask ^ (1 << city)
        city = p
    
    path.append(0)
    path.reverse()

    if path[-1] != 0:
        path.append(0)
    
    return best_cost, path


dist_matrix = [
#     0   1   2   3
    [ 0, 10, 15, 20], # 0
    [10,  0, 35, 25], # 1
    [15, 35,  0, 30], # 2
    [20, 25, 30,  0]  # 3
]

cost, route = solve(dist_matrix)

print("Min route:", cost)
print("Cities order:", route)
