import sys
read = sys.stdin.readline

cache = [0] * 11
cache[1] = 1
cache[2] = 2
cache[3] = 3

for i in range(3, 11):
    print(cache)
    cache[i] = sum(cache[i-3:i])

# T = int(read())
print(cache)
T = 5
for _ in range(T):
    print(cache[int(read())])



# 점화식으로 풀어내서 값을 구하는 방식이 있다. dfs로 통일하는 것이 좋아보인다.
# 아래는 DFS를 통해서 푸는 방법 풀이법은 점화식을 사용햇 규칙을 찾아낸 것이랑 똑같네?
# DP는 보통 점화식으로 풀이가 가능하다.

import sys
read = sys.stdin.readline

def dfs(num):
    if arr[num] > 0:
        return arr[num]
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        arr[num] = dfs(num - 1) + dfs(num - 2) + dfs(num - 3)
        return arr[num]


T = int(sys.stdin.readline())
for _ in range(T):
    l = int(read())
    arr = [0] * (l + 1)
    print(dfs(l))
