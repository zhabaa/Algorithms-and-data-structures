INF = 10 ** 9


def egg_drop_dp(eggs: int, floors: int) -> tuple[int, list[list[int]]]:
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]

    for f in range(1, floors + 1):
        dp[1][f] = f

    for e in range(2, eggs + 1):
        for f in range(1, floors + 1):
            best = INF

            for i in range(1, f + 1):
                worst = 1 + max(dp[e - 1][i - 1], dp[e][f - i])
                
                if worst < best:
                    best = worst
            
            dp[e][f] = best

    return dp[eggs][floors], dp

eggs = 2
floors = 100
min_throws, dp = egg_drop_dp(eggs, floors)
print(f"For {eggs} eggs and {floors} floors, min throws is {min_throws}")
