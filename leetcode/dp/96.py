# https://leetcode.com/problems/unique-binary-search-trees/
from functools import lru_cache

# 피보나치 수열을 이용한 방법이다
# 경우의 수를 구하는 것은 방법을 찾아서 진행하면 된다.
# 수열을 찾아서 진행해야 된다.
# 피보나치 수열을 이용한 방법이 아니다 카탙란 수열을 이용한 풀이다. 재귀를 통해서 풀 수 있다.
# 카탈란 수열은 1 1 2 5 14
# 피보나치 수열은 0 1 1 2 3 5
# 카탈란 수열을 안다면 쉽게 풀 수 있는 문제이다.
class Solution:
    @lru_cache(maxsize=None)
    def numTrees(self, n: int) -> int:
        if n <= 1: return 1
        return sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))