"""
https://leetcode.com/problems/two-sum/
"""


# o(n*n) brute force
def twoSumV1(nums, target):
    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if a + b == target and i != j:
                return [i, j]


# o(n) one pass
def twoSumV2(nums, target):
    store = {}
    for i, a in enumerate(nums):
        b = target - a
        j = store.get(b)

        if j is not None:
            return [j, i]

        store[a] = i
