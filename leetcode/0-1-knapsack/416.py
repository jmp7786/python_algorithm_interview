# https://leetcode.com/problems/partition-equal-subset-sum/
from functools import cache
# 짝수여야 풀 수 있는 문제다. 이 코드로 짝수 인지 확인한다. total_sum & 1 == 0
# dp에서 들어온 파라메터의 값으로 False값을 조절해야한다.


class Solution:
    def canPartition(self, nums):
        @cache
        def subsetSum(s, i):
            if s == 0: return True
            if i >= len(nums) or s < 0: return False
            return subsetSum(s-nums[i], i+1) or subsetSum(s, i+1)
        total_sum = sum(nums)
        return total_sum & 1 == 0 and subsetSum(total_sum // 2, 0)

print(2&1)