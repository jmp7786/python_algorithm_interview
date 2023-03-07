# https://leetcode.com/problems/product-of-array-except-self/
# 굉장히 좋은 문제다. n2으로 풀어야 하는 걸 n으로 줄이다니 특정한 경우에만 사용할 수 있는 건가?
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
