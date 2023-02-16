# https://leetcode.com/problems/house-robber/

import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = collections.OrderedDict()
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        self.dp[0], self.dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])


        return dp.popitem()[1]
