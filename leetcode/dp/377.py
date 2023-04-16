# https://leetcode.com/problems/combination-sum-iv/description/
# 아주 아름다운 풀이 방법이다. 경우의 수는 이렇게 풀어야겠다.
from typing import List

class Solution:
    dp = []

    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.dp = [-1] * (target+1)
        self.dp[0]= 1
        result = self.helper(nums, target)
        print(self.dp)
        return result

    def helper(self, nums, target):
        if self.dp[target] != -1:
            return self.dp[target]
        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.helper(nums, target-nums[i])
        self.dp[target] = res
        return res
