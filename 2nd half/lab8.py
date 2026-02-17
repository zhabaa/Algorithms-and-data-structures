import sys

amount = 5
coins = [1, 2, 5]

if amount < 0:
    print(0)
    sys.exit(1)

coins = sorted(set(coins))
dp = [0] * (amount + 1)
dp[0] = 1

for c in coins:
    for x in range(c, amount + 1):
        dp[x] += dp[x - c]

print(dp[amount])
# 4
# 5 = 5
# 5 = 2+2+1
# 5 = 2+1+1+1
# 5 = 1+1+1+1+1
