from typing import List, Tuple

def egg_drop_dp(eggs: int, floors: int) -> Tuple[int, List[List[int]]]:
    INF = 10 ** 9
    dp = [[0] * (floors+1) for _ in range(eggs + 1)]

    # 1 яйцо: только линейный поиск
    for f in range(1, floors+1):
        dp[1][f] = f

    for e in range(2, eggs+1):
        for f in range(1, floors+1):
            best = INF
            # x — этаж, с которого бросаем
            for x in range(1, f+1):
                # если разбилось -> e-1 яиц, x-1 этаж ниже
                # если не разбилось -> e яиц, f-x этаж выше
                worst = 1 + max(dp[e-1][x-1], dp[e][f-x])
                if worst < best:
                    best = worst
            dp[e][f] = best

    return dp[eggs][floors], dp

def strategy_two_eggs_100() -> List[int]:
    """
    Оптимальная известная стратегия для 2 яиц, 100 этажей:
    шаги 14,13,12,... пока не покроем 100.
    Возвращает этажи, с которых бросаем первое яйцо.
    """
    floors = 100
    step = 1
    # найдем минимальный t: t+(t-1)+...+1 >= floors
    t = 0
    s = 0
    while s < floors:
        t += 1
        s += t

    # теперь делаем прыжки t, t-1, ... , 1
    throws = []
    cur = 0
    for k in range(t, 0, -1):
        cur += k
        if cur > floors:
            cur = floors
        throws.append(cur)
        if cur == floors:
            break
    return throws

if __name__ == "__main__":
    min_throws, dp = egg_drop_dp(2, 100)
    print("DP min throws for 2 eggs, 100 floors =", min_throws)

    plan = strategy_two_eggs_100()
    print("First-egg floors:", plan)
