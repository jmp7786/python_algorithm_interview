# https://leetcode.com/problems/valid-palindrome/

import timeit
#대소문자 구분 x

# for 문을 사용해서 최적화함 3m 대
# class Solution:
#     def programmers-sping-test(self, s: str) -> bool:
#         lower_str = ''.join(filter(str.isalnum, s.lower()))
#         print(lower_str)
#         lower_str_len = len(lower_str)
#         string_middle_len = len(lower_str) // 2
#         for i in range(string_middle_len):
#             if (not (lower_str[i] == lower_str[-i - 1])):
#                 print(lower_str[i], i)
#                 print(lower_str[lower_str_len - i - 1])
#                 return False
#         return True

# 슬라이싱 할 경우 1ms 대로 내려간다.
class Solution:
    def test(self, s: str) -> bool:
        alnum_str = ''.join(filter(str.isalnum, s.lower()))
        return alnum_str == alnum_str[::-1]

if __name__ == '__main__':
    print(timeit.timeit("Solution().programmers-sping-test('A man, a plan, a canal: Panama')", setup="from __main__ import Solution", number=1))


