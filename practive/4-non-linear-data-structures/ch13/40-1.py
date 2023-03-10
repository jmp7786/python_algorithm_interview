# https://leetcode.com/problems/network-delay-time/
# 난이도가 있다.
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, K)]
        dist = collections.defaultdict(int)

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1


result = Solution().networkDelayTime([
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1],
], 4, 2)
print(result)

result = Solution().networkDelayTime([
    [3, 1, 5],
    [3, 2, 2],
    [2, 1, 2],
    [3, 4, 1],
    [4, 5, 1],
    [5, 6, 1],
    [6, 7, 1],
    [7, 8, 1],
    [8, 1, 1],
], 8, 3)
print(result)


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        Q = [(0, K)]
        dist = {}

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    heapq.heappush(Q, (w + time, v))

        return max(dist.values())


result = Solution().networkDelayTime([
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1],
], 4, 2)
print(result)

result = Solution().networkDelayTime([
    [3, 1, 5],
    [3, 2, 2],
    [2, 1, 2],
    [3, 4, 1],
    [4, 5, 1],
    [5, 6, 1],
    [6, 7, 1],
    [7, 8, 1],
    [8, 1, 1],
], 8, 3)
print(result)
