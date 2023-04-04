# https://leetcode.com/problems/find-all-duplicates-in-an-array/
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        memo = {}
        result = []
        for i in nums:
            if i in memo:
                result.append(i)
            else:
                memo[i] = 0
        return result