"""
Given a set of coin values coins={c1, c2, ..., ck} and 
a target sum of money m, in how many ways can we form the sum m using these coins?
"""


def how_many_ways(coins, m):
    memo = {}
    memo[0] = 1

    for i in range(1, m + 1):
        memo[i] = 0

        for coin in coins:
            subproblem = i - coin

            if subproblem < 0:
                continue

            memo[i] = memo[i] + memo[subproblem]

    return memo[m]


print(how_many_ways([1, 4, 5], 5))
