# https://www.acmicpc.net/problem/14889

import sys
from typing import List

N = int(input())
# #
graph= [[0] * N for _ in range(N)]
for j in range(N):
    raw = [int(i) for i in sys.stdin.readline().split()]
    for i in range(len(raw)):
        graph[j][i] = raw[i]

# 이중 포문을 돌면서 모든 경우의 수를 구한다.

# N = 4
# graph = [
# [0-1 knapsack, 1, 2, 3],
# [4, 0-1 knapsack, 5, 6],
# [7, 1, 0-1 knapsack, 2],
# [3, 4, 5, 0-1 knapsack]
# ]

# N = 6
# graph = [
# [0-1 knapsack, 1, 2, 3, 4, 5],
# [1, 0-1 knapsack, 2, 3, 4, 5],
# [1, 2, 0-1 knapsack, 3, 4, 5],
# [1, 2, 3, 0-1 knapsack, 4, 5],
# [1, 2, 3, 4, 0-1 knapsack, 5],
# [1, 2, 3, 4, 5, 0-1 knapsack]
# ]


result = sys.maxsize
original = [i for i in range(N)]
def dfs(path, depth):
    global result
    global original
    if depth == N//2:
        not_path = list(set(original) - set(path))
        a_point = getPoints(path)
        b_point = getPoints(not_path)

        calculate_point = abs(a_point - b_point)
        if result > calculate_point:
            result = calculate_point
    for e in path:
        new_path = path[:]
        new_path.remove(e)
        dfs(new_path, depth+1)

def getPoints(path: List[int]) -> int:
    result = 0
    for i in range(len(path)):
        for j in range(i+1, len(path)):
            result += graph[path[j]][path[i]] + graph[path[i]][path[j]]
    return result

t = [i for i in range(N)]
dfs(t, 0)
print(result)







'''
  1 2 3 4 5 6
1 0-1 knapsack 1 2 3 4 5
2 1 0-1 knapsack 2 3 4 5
3 1 2 0-1 knapsack 3 4 5
4 1 2 3 0-1 knapsack 4 5
5 1 2 3 4 0-1 knapsack 5
6 1 2 3 4 5 0-1 knapsack

1,3,6
=> [1,3](2+1) + [1,6](5+1) + [3,6](5+3) => 3+6+8 = 17  
2,4,5
=> [2,4](2+3) + [2,5](2+4) + [4,5](4+4) => 5+6+8 = 19
'''