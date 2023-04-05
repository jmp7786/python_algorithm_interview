# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
from collections import Counter
from typing import List


def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    c = Counter(arr)
    s = sorted(arr, key=lambda x: (c[x], x))
    return len(set(s[k:]))

