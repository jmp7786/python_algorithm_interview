# https://leetcode.com/problems/single-number/
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result

result = Solution().singleNumber([2,1,2])
print(result)