# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = [x**2 for x in nums]
        new.sort()
        return new