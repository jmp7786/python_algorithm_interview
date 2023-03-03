# 연결되어 있는 그래프를 그리면 될듯~?
import collections


count = 0
def findHouses(s):
    global count
    def dfs(s, i, j):
        if i < 0 or i > len(s) -1 or j < 0 or j > len(s[0])-1 or s[i][j] != 1:
            return False


        s[i][j] = 0
        dfs(s, i-1, j)
        dfs(s, i+1, j)
        dfs(s, i, j-1)
        dfs(s, i, j+1)

        global count
        count = count + 1
        print(count)
        return True

    result = []
    for i in range(len(s)):
        for j in range(len(s[0])):
            if dfs(s, i, j):
                result.append(count)
                count = 0

    return sorted(result)





result = findHouses([
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0],
])
print(len(result), result)

# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
# 연결되어 있는 그래프를 그리면 될듯~?
import collections

count = 0

class House:
    count = 1
    def findHouses(self, s):
        result = []
        for i in range(len(s)):
            for j in range(len(s[0])):
                if self.__dfs(s, i, j):
                    result.append(count)
                    self.count = 0

        return sorted(result)
    def __dfs(self, s,i, j):
        if i < 0 or i > len(s) - 1 or j < 0 or j > len(s[0]) - 1 or s[i][j] != 1:
            return False

        s[i][j] = 0
        self.__dfs(s, i - 1, j)
        self.__dfs(s, i + 1, j)
        self.__dfs(s, i, j - 1)
        self.__dfs(s, i, j + 1)

        self.count += 1
        return True


def findHouses(s):
    count = 1
    def dfs(s, i, j):
        if i < 0 or i > len(s) - 1 or j < 0 or j > len(s[0]) - 1 or s[i][j] != 1:
            return False

        s[i][j] = 0
        dfs(s, i - 1, j)
        dfs(s, i + 1, j)
        dfs(s, i, j - 1)
        dfs(s, i, j + 1)

        count = count + 1
        return True

    result = []
    for i in range(len(s)):
        for j in range(len(s[0])):
            if dfs(s, i, j):
                result.append(count)
                count = 0

    return sorted(result)


result = findHouses([
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0],
])
print()
print(len(result))
for i in range(len(result)):
    print(result[i])

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


# n = int(input())
n = 7
# graph = []
graph = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0],
]
# for i in range(n):
#     graph.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])


class House:
    count = 0

    def findHouses(self, s):
        result = []
        for i in range(len(s)):
            for j in range(len(s[0])):
                if self.__dfs(s, i, j):
                    result.append(self.count)
                    self.count = 0

        return sorted(result)

    def __dfs(self, s, i, j):
        if i < 0 or i > len(s) - 1 or j < 0 or j > len(s[0]) - 1 or s[i][j] != '1':
            return False

        s[i][j] = 0
        self.count += 1

        self.__dfs(s, i - 1, j)
        self.__dfs(s, i + 1, j)
        self.__dfs(s, i, j - 1)
        self.__dfs(s, i, j + 1)


        return True


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = House().findHouses(graph)
print(result)
