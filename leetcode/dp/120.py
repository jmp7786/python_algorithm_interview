# https://leetcode.com/problems/triangle/description/
# 풀었는데 속도가 너무 느리네? print()가 들어감 April 7, 2023 Friday
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