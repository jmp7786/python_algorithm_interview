# https://leetcode.com/problems/minimum-path-sum/
from typing import List
# 역시 memoization의 코드가 훨씬 깔끔하다. 속도는 약간 느림 가독성도 좋으므로 memoization으로 연습하자.


#tabulation
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        for j in range(1, n):
            for i in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]

#Memoization
from functools import lru_cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return float('inf')

            return grid[i][j] + min(dp(i-1, j), dp(i, j-1))

        return dp(m-1, n-1)
