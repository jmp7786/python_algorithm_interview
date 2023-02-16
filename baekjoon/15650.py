import sys
input = sys.stdin.readline
n, m = map(int, input().split())

path = []
def dfs():
    if len(path) == m:
        print(' '.join(path))
        return

    for i in range(1, n+1):
        if i not in path:
            path.append(str(i))
            dfs()
            path.remove(str(i))


dfs()