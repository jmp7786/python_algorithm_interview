# https://leetcode.com/problems/house-robber
# 213 형제 문제
# 할줄만 알면 아주 쉽다.
# 문제 품 April 7, 2023 Friday

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]
