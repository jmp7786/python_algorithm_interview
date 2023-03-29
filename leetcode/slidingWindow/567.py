# https://leetcode.com/problems/permutation-in-string/
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        char_count_s1, char_count_window = Counter(s1), Counter(s2[:len_s1])

        for i in range(len_s1, len_s2):
            if char_count_s1 == char_count_window:
                return True

            char_count_window[s2[i - len_s1]] -= 1
            char_count_window[s2[i]] += 1

        return char_count_s1 == char_count_window