# https://leetcode.com/problems/unique-paths-ii/
from functools import lru_cache
from typing import List



#내 풀이
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m >= 1 and n >= 1:
            if obstacleGrid[0][0] == 1:
                return 0

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0

            if i + 1 <= m - 1 and obstacleGrid[i + 1][j] == 1 and j + 1 <= n - 1 and obstacleGrid[i][j + 1] == 1:
                return 0
            elif i + 1 <= m - 1 and obstacleGrid[i + 1][j] == 1:
                return dfs(i, j + 1)
            elif j + 1 <= n - 1 and obstacleGrid[i][j + 1] == 1:
                return dfs(i + 1, j)

            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)

