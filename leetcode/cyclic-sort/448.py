# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        result = []
        for i in range(1, len(nums)+1):
            if i not in num_set:
                result.append(i)
        return result
