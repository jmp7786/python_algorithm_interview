# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort = sorted(nums)
        left = 0
        right = len(nums) - 1
        if sort == nums or len(nums) == 1:
            return 0
        for x in range(len(nums)):
            if nums[left] == sort[left]:
                left += 1
            if nums[right] == sort[right]:
                right -= 1
            if left == right:
                return 0
        return right - left + 1
