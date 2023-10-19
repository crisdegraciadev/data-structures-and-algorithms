"""Given a n number, calculate his fibonnaci value"""


# Slow and intensive memory usage
def fib_rec(n):
    return n if n <= 2 else fib_rec(n - 1) + fib_rec(n - 2)


# Dynamic programming = Solve subproblems + Memoization
memo = {}


def fib_dy(n):
    if n in memo:
        return memo.get(n)

    if n <= 2:
        result = 1
    else:
        result = fib_dy(n - 1) + fib_dy(n - 2)

    memo[n] = result

    return result


def fib_dy_bottom_up(n):
    for i in range(1, n + 1):
        if n <= 2:
            result = 1
        else:
            result = memo[n - 1] + memo[n - 2]

        memo[i] = result

    return memo[n]


print(fib_dy(500))
