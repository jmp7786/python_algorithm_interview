# https://leetcode.com/problems/triangle/description/

from functools import lru_cache
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dfs(depth: int, i: int):
            if depth == len(triangle):
                return 0

            leftButtom = dfs(depth + 1, i)
            rightButtom = dfs(depth + 1, i + 1)

            return min(triangle[depth][i] + leftButtom, triangle[depth][i] + rightButtom)

        return dfs(0, 0)