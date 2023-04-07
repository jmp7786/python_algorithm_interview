# https://leetcode.com/problems/maximum-product-subarray/
# 아름다운 알고리즘이다.
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = nums
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)
