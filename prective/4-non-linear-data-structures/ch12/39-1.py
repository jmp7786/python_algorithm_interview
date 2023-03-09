# https://leetcode.com/problems/course-schedule/
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True
result = Solution().canFinish(2,[[1,0]])
print(result)

result = Solution().canFinish(2,[[1,0],[0,1]])
print(result)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for i, j in prerequisites:
            graph[i].append(j)

        traced = set()
        visited = set()
        def dfs(node):
            if node in traced:
                return False
            if node in visited:
                return True


            traced.add(node)
            for n in graph[node]:
                if not dfs(n):
                    return False

            traced.remove(node)
            visited.add(node)

            return True

        for n in list(graph):
            if not dfs(n):
                return False

        return True



result = Solution().canFinish(2,[[1,0]])
print(result)

result = Solution().canFinish(2,[[1,0],[0,1]])
print(result)