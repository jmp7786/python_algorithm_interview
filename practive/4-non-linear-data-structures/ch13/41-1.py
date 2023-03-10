# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# 책에서 나온 해결방법으로는 해결이 안된다. TC가 추가되면서 막힌듯
import collections
import heapq
from typing import List


# 벨만 포드 알고리즘으로 푸는 방식으로 변경해야 한다.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices[:]
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices

        return -1 if prices[dst] == float('inf') else prices[dst]


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1


result = Solution().findCheapestPrice(3, [
    [0, 1, 100],
    [1, 2, 100],
    [0, 2, 500],
], 0, 2, 0)
print(result)


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for f, t, p in flights:
            graph[f].append((t, p))

        Q = [(0, src, K)]

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for t, p in graph[node]:
                    heapq.heappush(Q, (p + price, t, k-1))
        return -1


result = Solution().findCheapestPrice(3, [
    [0, 1, 100],
    [1, 2, 100],
    [0, 2, 500],
], 0, 2, 0)
print(result)
