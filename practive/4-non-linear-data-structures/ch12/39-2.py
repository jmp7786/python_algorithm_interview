import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문했던 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

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

        visited = []
        traced = []

        def dfs(node):
            if node in visited:
                return True
            if node in traced:
                return False

            traced.append(node)
            for i in graph[node]:
                if not dfs(i):
                    return False

            traced.remove(node)
            visited.append(node)

            return True

        for i in list(graph):
            if not dfs(i):
                return False

        return True

result = Solution().canFinish(2,[[1,0]])
print(result)

result = Solution().canFinish(2,[[1,0],[0,1]])
print(result)

