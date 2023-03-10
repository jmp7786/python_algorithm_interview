# https://leetcode.com/problems/permutations/
# parmutation과 combination의 접근 방법이 조금 다르네
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

result = Solution().permute([1,2,3, 4])
print(result)


import itertools
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
result = Solution().permute([1,2,3])
print(result)



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []
        def dfs(elements):
            if not elements:
                result.append(prev_elements[:])
                return

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.remove(e)

        dfs(nums)
        return result


result = Solution().permute([1,2,3])
print('answer', result)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
result = Solution().permute([1, 2, 3])
print(result)
