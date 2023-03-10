# https://leetcode.com/problems/combination-sum/
# 조합은 중복을 없애야 한다. 그러기 위해서는 반복문을 돌릴 경우 하위 원소만 돌리도록 해야한다.
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result
result = Solution().combinationSum([2,3,6,7], 7)
print(result)
result = Solution().combinationSum([2,3,5], 8)
print(result)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], 0, path + [candidates[i]])

        dfs(target, 0, [])
        return result

result = Solution().combinationSum([2,3,6,7], 7)
print(result)
result = Solution().combinationSum([2,3,5], 8)
print(result)
print('----------------------------------------------------------------------')

class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        result = []
        def dfs(csum: int, index: int, path: List[int]):
            if csum < 0:
                return
            if csum == 0:
                result.append(path[:])
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], 0, path + [candidates[i]])

        dfs(target, 0, [])
        return result

result = Solution().combinationSum([2,3,6,7], 7)
print(result)
result = Solution().combinationSum([2,3,5], 8)
print(result)


class Solution3:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        result = []
        def dfs(csum, index, path):
            if csum == target:
                result.append(path[:])
                return
            if csum > target:
                return
            for i in range(index, len(candidates)):
                dfs(csum +candidates[i], 0, path + [candidates[i]])
        dfs(0, 0, [])
        return result


# result = Solution().combinationSum([2,3,6,7], 7)
# print(result)
result2 = Solution3().combinationSum([2,3,5], 8)
print(3, result2)
