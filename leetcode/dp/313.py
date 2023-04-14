# https://leetcode.com/problems/super-ugly-number/
import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        starts, nums = [0] * k, [1]
        for i in range(n - 1):
            candidates = [primes[j] * nums[starts[j]] for j in range(k)]
            new_num = min(candidates)
            nums.append(new_num)
            starts = [starts[i] + (candidates[i] == new_num) for i in range(k)]

        return nums[-1]
