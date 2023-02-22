# 최단거리는 BFS를 통해서 풀아야 한다.
import collections
from typing import List

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]


def bfs(s: List[List[int]], n: int, m: int):
    q = collections.deque()
    q.append((0, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] == 1:
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] +1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] +1

    return visited[len(s)-1][len(s[0])-1]

result = bfs(graph, n, m)
print(result)
