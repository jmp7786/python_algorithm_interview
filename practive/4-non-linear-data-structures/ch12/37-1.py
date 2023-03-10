# https://leetcode.com/problems/subsets/
# combination에서 스스로의 걍우의 수를 포함하면 i로 아니라면 i+1을 사용한다.
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # 매 번 결과 추가
            result.append(path)

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result


result = Solution().subsets([1, 2, 3])
print(result)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path, index):
            result.append(path)
            for i in range(index, len(nums)):
                dfs(path +[nums[i]], i+1 )
        dfs([], 0)
        return result

result = Solution().subsets([1, 2, 3])
print(result)
