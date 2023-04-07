# https://leetcode.com/problems/jump-game-ii/description/
# 좋은 dp 문제이다.

from functools import lru_cache
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i):
            if i == n - 1: return 0  # Reached to last index
            ans = float('inf')
            maxJump = min(n - 1, i + nums[i])
            for j in range(i + 1, maxJump + 1):
                ans = min(ans, dp(j) + 1)
            return ans

        return dp(0)