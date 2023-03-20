# https://leetcode.com/problems/majority-element/
# 3, 4번으로 풀이
# 매우 쉽다.
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num
