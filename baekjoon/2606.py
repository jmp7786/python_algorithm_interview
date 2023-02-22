# 연결되어 있는 그래프를 그리면 될듯~?
import collections


def findGraph(s):
    graph = collections.defaultdict(list)
    for n, t in s:
        graph[n].append(t)

    q = [graph[1].pop()]

    count = 0
    while q:
        n = q.pop()
        count += 1
        for _ in range(len(graph[n])):
            target = graph[n].pop()
            q.append(target)

    return count




result = findGraph([
    [1,2],
    [2,3],
    [1,5],
    [5,2],
    [5,6],
    [4,7],
])
print(result)