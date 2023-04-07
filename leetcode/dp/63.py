# https://leetcode.com/problems/unique-paths-ii/
from functools import lru_cache
from typing import List



#내 풀이
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m * n >= 1 and obstacleGrid[0][0] == 1:
            return 0

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            if obstacleGrid[i][j]:  # hit an obstacle
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dp(i + 1, j) + dp(i, j + 1)

        return dp(0, 0)