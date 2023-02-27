# https://leetcode.com/problems/trapping-rain-water/
import timeit
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0

        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left +=1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


if __name__ == '__main__':
    print(timeit.timeit("print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))",
                        setup="from __main__ import Solution", number=1))
