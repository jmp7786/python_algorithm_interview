# https://leetcode.com/problems/interleaving-string/
# 재미있는 문제였다. 비슷한 문제를 보지는 못했음
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3): return False

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            if i == n and j == m: return True
            ans = False
            if i < n and s1[i] == s3[i + j]:
                ans |= dp(i + 1, j)
            if j < m and s2[j] == s3[i + j]:
                ans |= dp(i, j + 1)

            return ans

        return dp(0, 0)









