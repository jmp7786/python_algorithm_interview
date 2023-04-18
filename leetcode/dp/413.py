# https://leetcode.com/problems/arithmetic-slices/
# 스스로 풀었다. 계속 푸니까 직관이 생긴 것 같다.
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        for i in range(2, len(nums)):
            diff = nums[i - 1] - nums[i - 2]
            if diff == nums[i] - nums[i - 1]:
                count += 1
                for j in range(i + 1, len(nums)):
                    if diff == nums[j] - nums[j - 1]:
                        count += 1
                    else:
                        break
            else:
                continue

        return count

