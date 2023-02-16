import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results


result = Solution().combine(5, 3)
print(result)

from typing import List


# 수식 nCr = n!/k!(n-k)!
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements: List[int], start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results


result = Solution().combine(5, 3)
print(result, len(result))


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


result = Solution().combine(5, 3)
print(result, len(result))


# 수식 nCr = n!/k!(n-k)!
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(path, index, remain):
            if remain <= 0:
                result.append(path[:])
                return

            for i in range(index, n+1):
                dfs(path + [i], i+1, remain - 1)

        dfs([], 1, k)

        return result


result = Solution().combine(5, 3)
print(result, len(result))


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1),k ))


result = Solution().combine(5, 3)
print(result, len(result))
