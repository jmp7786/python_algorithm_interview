# 새로운 응용 유형이다. dfs를 어떻게 사용해야 하는지 알 것 같다. 아직 새로운 유형에서는 어떻게 접근해야 할지 감이 안 온다.
# 목 연산을 //로 사용하면 틀린다. int()로 사용해야 한다.
# 소름 돋는 걸 발견했다. -1.666은 -2로 변환된다. 버림이 아니라 내림이기 때문이다.
# 해냈다. //을 사용해서 정답을 맞췄다.
import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)


dfs(1, nums[0], op[0], op[1], op[2], op[3])

print(maximum)
print(minimum)
print(int(10 / 0))


import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        if nums[depth] != 0:
            if total < 0:
                dfs(depth + 1, -((-total) // nums[depth]), plus, minus, multiply, divide - 1)
            else:
                dfs(depth + 1, total // nums[depth], plus, minus, multiply, divide - 1)


dfs(1, nums[0], op[0], op[1], op[2], op[3])

print(maximum)
print(minimum)
