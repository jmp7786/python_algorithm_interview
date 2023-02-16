import sys
sys.setrecursionlimit(10**6)

# n, m = list(map(int, input().split()))
n, m = 3, 3

path = []
visited = []
def dfs():
    if len(path) == m:
        _path = ' '.join(path)
        if _path not in visited:
            visited.append(_path)
            print(_path)
        return

    for i in range(1, n+1):
        if i not in path:
            path.append(str(i))
            dfs()
            path.remove(str(i))

dfs()
