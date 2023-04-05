# https://leetcode.com/problems/find-right-interval/
from bisect import bisect
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ints = sorted([[j, k, i] for i, [j, k] in enumerate(intervals)])
        begs = [i for i, _, _ in ints]
        out = [-1] * len(begs)
        for i, j, k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                out[k] = ints[t][2]

        return out
