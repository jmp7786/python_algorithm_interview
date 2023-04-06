# https://leetcode.com/problems/unique-paths/
from functools import lru_cache


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @lru_cache(maxsize=None)
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)