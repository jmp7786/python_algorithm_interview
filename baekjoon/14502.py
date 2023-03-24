# www.acmicpc.net/problem/14502
# 해답 https://cotak.tistory.com/14
# 어려운 문제다. 벽을 어떻게 새워야 하는지 감을 잡기 쉽지 않다.
# 코드의 양도 많다.
# 하단의 설명
import sys, copy, collections
from typing import List

n, m = map(int, sys.stdin.readline().split())
max_num = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
empty_list = []
virus_list = []

EMPTY = 0
WALL = 1
VIRUS = 2

# 입력
g = [[0] * m for _ in range(n)]

for y in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]

    for x in range(m):
        g[y][x] = raw[x]
        if g[y][x] == EMPTY:
            empty_list.append([y, x])
        if g[y][x] == VIRUS:
            virus_list.append([y, x])


# bfs 탐색
def bfs(ng):
    q = collections.deque([])
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    global max_num

    for virus in virus_list:
        q.append(virus)

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if ng[ny][nx] == EMPTY and visited[ny][nx] == False:
                q.append([ny, nx])
                ng[ny][nx] = VIRUS
                visited[ny][nx] = True

    for i in range(n):
        cnt += ng[i].count(EMPTY)

    if max_num < cnt:
        max_num = cnt


# 벽 세우기
for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            g[y1][x1] = WALL
            g[y2][x2] = WALL
            g[y3][x3] = WALL

            ng = copy.deepcopy(g)
            bfs(ng)

            g[y1][x1] = EMPTY
            g[y2][x2] = EMPTY
            g[y3][x3] = EMPTY

print(max_num)

'''
코드를 더 구체적으로 설명하겠습니다. 주요 변수와 함수에 대한 설명을 추가하였습니다.

변수 정의

n, m: 연구소의 크기 (행, 열)
max_num: 안전 영역의 최대 크기
dx, dy: 4방향 이동을 위한 x, y 좌표의 변화값
EMPTY, WALL, VIRUS: 빈 칸, 벽, 바이러스를 의미하는 상수
g: 연구소의 초기 상태를 저장하는 2차원 리스트
empty_list: 빈 칸의 위치를 저장하는 리스트
virus_list: 바이러스의 위치를 저장하는 리스트
입력 받기

n과 m을 입력 받아 연구소의 크기를 저장합니다.
연구소의 초기 상태를 입력 받아 2차원 리스트 g에 저장하고, 빈 칸과 바이러스의 위치를 각각 empty_list와 virus_list에 저장합니다.
bfs 함수

바이러스를 퍼뜨리는 과정을 구현하는 함수입니다.
입력: 새로운 연구소 지도(ng)
ng에서 각 바이러스의 위치를 시작점으로 하여 BFS를 수행합니다.
큐(q)가 빌 때까지 반복하며, 상하좌우로 인접한 빈 칸에 바이러스를 전파시킵니다.
바이러스가 전파된 후의 연구소 상태를 반환합니다.
벽 세우기

빈 칸(empty_list)의 모든 조합에 대해 벽을 세워 봅니다.
세 개의 벽을 세운 후에 bfs 함수를 호출하여 바이러스를 퍼뜨린 후의 연구소 상태(ng)를 얻습니다.
바이러스가 퍼진 후의 연구소 상태에서 안전 영역의 크기를 계산하고, 최대값을 업데이트합니다.
안전 영역의 크기는 빈 칸(EMPTY)의 개수로 계산합니다.
벽을 세운 후에는 원래 상태로 되돌립니다.
결과 출력

안전 영역의 최댓값(max_num)을 출력합니다.
코드는 이러한 과정을 통해 모든 가능한 벽 조합을 시도하고, 각 경우에 대해 바이러스를 퍼뜨려서 안전 영역의 최대 크기를 구합니다. 이 과정은 주어진 문제를 해결하는 데 충분하지만, 효율성을 개선하기 위해 백트래킹 등의 방법을 적용할 수도 있습니다.
'''

import sys, copy, collections
from typing import List

N, M = map(int, sys.stdin.readline().split())
# N, M = 3, 4
max_num = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
empty_list = []
virus_list = []

EMPTY = 0
WALL = 1
VIRUS = 2
graph = [[0] * M for _ in range(N)]

for y in range(N):
    raw = [int(x) for x in sys.stdin.readline().split()]

    for x in range(M):
        graph[y][x] = raw[x]
        if graph[y][x] == EMPTY:
            empty_list.append([y, x])
        if graph[y][x] == VIRUS:
            virus_list.append([y, x])


def bfs(new_graph: List[List[int]]) -> None:
    q = collections.deque([])
    visited = [[False * M] for _ in range(N)]
    count = 0

    global max_num

    for virus in virus_list:
        q.append(virus)

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if new_graph[ny][nx] == EMPTY and visited[ny][nx] == False:
                q.append([ny, nx])
                ng[ny][nx] = VIRUS
                visited[ny][nx] = True

    for i in range(n):
        count += new_graph[i].count(EMPTY)
    if max_num < count:
        max_num = count


for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            graph[y1][x1] = WALL
            graph[y2][x2] = WALL
            graph[y3][x3] = WALL

            new_graph = copy.deepcopy(graph)
            bfs(new_graph)

            graph[y1][x1] = EMPTY
            graph[y2][x2] = EMPTY
            graph[y3][x3] = EMPTY

print(max_num)









# ----------------------------------------------------------------------
import sys, copy, collections

n, m = map(int, sys.stdin.readline().split())
max_num = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
empty_list = []
virus_list = []

EMPTY = 0
WALL = 1
VIRUS = 2

# 입력
g = [[0] * m for _ in range(n)]

for y in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]

    for x in range(m):
        g[y][x] = raw[x]
        if g[y][x] == EMPTY:
            empty_list.append([y, x])
        if g[y][x] == VIRUS:
            virus_list.append([y, x])


def bfs(ng):
    q = collections.deque([])
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    global max_num

    for virus in virus_list:
        q.append(virus)

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if ng[ny][nx] == EMPTY and visited[ny][nx] == False:
                q.append([ny, nx])
                ng[ny][nx] = VIRUS
                visited[ny][nx] = True

    for i in range(n):
        cnt += ng[i].count(EMPTY)

    if max_num < cnt:
        max_num = cnt



for i in range(len(empty_list)):
    for j in range(i + 1, len(empty_list)):
        for k in range(j + 1, len(empty_list)):
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            g[y1][x1] = WALL
            g[y2][x2] = WALL
            g[y3][x3] = WALL

            ng = copy.deepcopy(g)
            bfs(ng)

            g[y1][x1] = EMPTY
            g[y2][x2] = EMPTY
            g[y3][x3] = EMPTY

print(max_num)