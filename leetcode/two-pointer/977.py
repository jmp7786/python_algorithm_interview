# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right  = 0, n-1
        k = n-1
        new_nums = [0] * n
        while k >= 0:
            if abs(nums[left]) > abs(nums[right]):
                new_nums[k] = nums[left] * nums[left]
                left +=1
            else:
                new_nums[k] = nums[right] * nums[right]
                right -= 1
            k -= 1
        return new_nums

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = [x**2 for x in nums]
        new.sort()
        return new
