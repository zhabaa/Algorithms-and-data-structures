def change_coins(amount: int, coins: list[int]) -> int:
    if amount < 0:
        return 0

    coins = sorted(set(coins))

    dp = [0] * (amount + 1)
    dp[0] = 1

    for c in coins:
        for i in range(c, amount + 1):
            dp[i] += dp[i - c]

    return dp[amount]


amount = 100
coins = [1, 2, 5, 10]

print(change_coins(amount, coins))

# 4
# 5 = 5
# 5 = 2 + 2 + 1 
# 5 = 2 + 1 + 1 + 1
# 5 = 1 + 1 + 1 + 1 + 1
