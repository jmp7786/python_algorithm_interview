# https://leetcode.com/problems/longest-palindromic-substring/
import timeit

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expends(left: int, right:int) -> str:
            while left >=0 and right < len(s) and s[left] == s[right]:
                left-= 1
                right += 1
            return s[left+1: right]

        if s == s[::-1] or len(s) < 2:
            return s

        result = ''
        for i in range(len(s)-1):
            result = max(result, expends(i, i+1), expends(i, i+2), key=len)
        print(result)
        return result

if __name__ == '__main__':
    print(timeit.timeit("Solution().longestPalindrome('1ccddddaaaacd1Ra11111111')", setup="from __main__ import Solution", number=1))
