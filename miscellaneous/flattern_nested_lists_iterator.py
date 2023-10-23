"""
https://leetcode.com/problems/flatten-nested-list-iterator/
"""

from typing import List


class NestedInteger:
    def is_integer(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def get_integer(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def get_list(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nested_list: List[NestedInteger]):
        self.stack = []
        self.dfs(nested_list)
        self.stack.reverse()

    def next(self) -> int:
        return self.stack.pop()

    def has_next(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, nested):
        for n in nested:
            if n.isInteger():
                self.stack.append(n.getInteger())
            else:
                self.dfs(n.getList())
