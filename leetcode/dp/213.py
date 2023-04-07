# https://leetcode.com/problems/house-robber-ii/
# 복습할 것 April 6, 2023 Thursday
# memoization의 적다 tabulation이 어울리는 문제다.
# rob은 좀 어렵네
# 잘 풀었다. April 7, 2023 Friday

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ## RC ##
        ## APPROACH : DP ##
        ## LOGIC ##
        ## 1. Only 2 scenarios possible
        ##     a) Rob 1st and donot rob last
        ##     b) Rob last and donot rob first.
        ## We take maximum of both cases.

        ## TIME COMPLEXITY : O(N) ##
        ## SPACE COMPLEXITY : O(N) ##

        def house_robber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            return max(dp[-1], dp[-2])

        if len(nums) <= 2: return max([0] + nums)
        return max(house_robber(nums[1:]), house_robber(nums[:-1]))

