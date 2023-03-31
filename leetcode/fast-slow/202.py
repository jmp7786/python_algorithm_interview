# https://leetcode.com/problems/happy-number/description/
# fast and slow 기법을 사용해서 툰 솔루션이 없는데 블로그의 강의에서만 사용한 것 같다.
# 그냥 문제를 보고 품 유형에는 안 맞는듯

class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        while n > 0:
            if n in visited:
                return False

            visited.add(n)
            result = 0
            for char in str(n):
                char_num = int(char)
                result += char_num * char_num
            if result == 1:
                return True

            n = result

        return False