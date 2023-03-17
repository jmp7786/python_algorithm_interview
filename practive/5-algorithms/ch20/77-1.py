# https://leetcode.com/problems/longest-repeating-character-replacement/
# 이건 이해가 잘 안되네

import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left

result = Solution().characterReplacement("ABAB", 2)
print(result)




'''
What is the difference between throw and throws in Java?
How does the assert keyword work in Java?
What is the difference between private, protected, and public access modifiers in Java?
What is the difference between break and continue in Java?
What is the difference between a HashSet and a LinkedHashSet in Java?
What is the difference between a HashMap and a LinkedHashMap in Java?
What is the difference between an ArrayList and a LinkedList in Java?
What is the purpose of the Comparable interface in Java?
What is the purpose of the Iterator interface in Java?
What is the purpose of the ListIterator interface in Java?
What is a lambda expression in Java?
What is a method reference in Java?
What is the Optional class in Java 8?
What is a functional interface in Java?
What is the default method in Java 8?
What is the purpose of the @Override annotation in Java?
What is the purpose of the @FunctionalInterface annotation in Java?
What is the purpose of the @Deprecated annotation in Java?
What is a Java Bean in Java?
What is the Observer pattern in Java?
What is the Singleton pattern in Java?
What is the Factory pattern in Java?
What is the Abstract Factory pattern in Java?
What is the Builder pattern in Java?
What is the Prototype pattern in Java?
What is the Adapter pattern in Java?
What is the Decorator pattern in Java?
What is the Facade pattern in Java?
What is the Proxy pattern in Java?
What is the Chain of Responsibility pattern in Java?
'''