"""
Given an NxM grid, in how many ways can a rabbit get from the top-left
to the bottom right corner if it can only move down and right?
"""


def grid_paths(n, m):
    memo = {}

    # BASE CASES
    #
    # if n == 1 and m == 1:
    #     return 1
    #
    # if n == 1:
    #     return m
    #
    # if m == 1:
    #     return n
    #
    # The memo stores how many paths can we take
    # to arrive at a position

    for i in range(1, n + 1):
        memo[(i, 1)] = 1

    for j in range(1, m + 1):
        memo[(1, j)] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]
            print(memo)

    return memo[(n, m)]


print(grid_paths(3, 3))
