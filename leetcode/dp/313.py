# https://leetcode.com/problems/super-ugly-number/
import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        cand = [(p, p, 1) for p in primes]
        ugly = [1]
        for _ in range(n-1):
            ugly.append(cand[0][0])
            while cand[0][0] == ugly[-1]:
                x, p, i = heapq.heappop(cand)
                heapq.heappush(cand, (p*ugly[i], p, i+1))
        return ugly[-1]