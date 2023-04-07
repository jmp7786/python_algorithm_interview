# https://leetcode.com/problems/interleaving-string/
# 재미있는 문제였다. 비슷한 문제를 보지는 못했음
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3): return False

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            if i == n and j == m: return True
            ans = False
            if i < n and s1[i] == s3[i + j]:
                ans |= dp(i + 1, j)
            if j < m and s2[j] == s3[i + j]:
                ans |= dp(i, j + 1)

            return ans

        return dp(0, 0)

# 아래는 잘못된 코드이다.
# 잘못 들어간 포인트는
# 1. maxsize를 i> s1_n and j > s2_n으로 해야되는데 잘못 되었음
# 2. i와 j를 늘리는 구간에 i, j의 크기를 제한하지 않음. -> 두 가지의 인덱스가 돌 경우에는 다른 쪽의 접근으로 커진 인덱스가 지속적으로 돌 위험이 있다.
#    커진 채로 도는 녀석을 n보타 커지지 않도록 조건을 걸어줘야 한다.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_n, s2_n, s3_n = len(s1), len(s2), len(s3)

        if s1_n + s2_n != s3_n:
            return False
        if s1_n + s2_n + s3_n == 0 or (s1 == s3 and not s2) or (s2 == s3 and not s1):
            return True

        def dp(i, j):

            if i >= s1_n or j >= s2_n:
                return False
            print(i, j, s1[i], s2[j], s3[i + j])
            if i == s1_n - 1 and j == s2_n - 1:
                return True

            ans = False
            if s1[i] == s3[i + j]:
                ans |= dp(i + 1, j)

            if s2[j] == s3[i + j]:
                ans |= dp(i, j + 1)

            return ans

        return dp(0, 0)





