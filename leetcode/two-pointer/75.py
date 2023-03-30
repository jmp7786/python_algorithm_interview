# https://leetcode.com/problems/sort-colors/description/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """j
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1
