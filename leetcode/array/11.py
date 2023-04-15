
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        amount = 0
        # indexed_height = [[i, v]for i in enumerate(hieght)]
        # sorted(indexed_height, key=lambda x: x[1])
        while left < right:
            dam_size = min(height[left], height[right])
            amount = max(amount, dam_size * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return amount


