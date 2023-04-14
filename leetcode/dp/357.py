# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
'''
O(1)로 풀 수 있는 답이 정해져 있는 문제 상수 시간으로 돌면 O(1)이다.
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        res = 10
        digits = 9
        availableNumber = 9
        while n  > 1 and availableNumber > 0:
            n -= 1
            digits = digits * availableNumber
            res += digits
            availableNumber -=1
        return res
