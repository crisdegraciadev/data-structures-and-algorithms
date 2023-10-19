"""
Given a set of coin values coins={c1, c2, ..., ck} and 
a target sum of money m, what's the minimum number of coins that form the sum m?
"""


memo = {}


def min_ignore_none(a, b):
    if a is None:
        return b

    if b is None:
        return a

    return min(a, b)


def min_coins(coins, m):
    if m in memo:
        return memo[m]

    if m == 0:
        result = 0
    else:
        result = None
        for coin in coins:
            subproblem = m - coin

            if subproblem < 0:
                continue

            step = min_coins(coins, subproblem)

            if step is None:
                return None

            result = min_ignore_none(result, step + 1)

    memo[m] = result

    return result


def min_coins_up_to_bottom(coins, m):
    memo[0] = 0

    for i in range(1, m + 1):
        for coin in coins:
            subproblem = i - coin

            if subproblem < 0:
                continue

            step = memo.get(subproblem)

            if step is None:
                return None

            # If there is already a best solution, take it
            memo[i] = min_ignore_none(memo.get(i), step + 1)

        print("")
        print(memo)
        print(f"memoized value={memo[i]}")

    return memo[m]


print(min_coins_up_to_bottom([1, 4, 5], 13) or 0)
