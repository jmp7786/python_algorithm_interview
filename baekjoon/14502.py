# https://www.acmicpc.net/problem/14501
# 집도둑과 같은 유형의 문제이다.

# 타뷸레이션(bottom-up)
# import sys
# N = int(input())
#
# schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
#
# dp = [0 for i in range(N+1)]
#
# for i in range(N):
#     for j in range(i+schedule[i][0], N+1):
#         if dp[j] < dp[i] + schedule[i][1]:
#             dp[j] = dp[i] + schedule[i][1]
#
# print(dp[-1])
#
#
# # 메모이제이션(top-down)
N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]


N = 7
dp = [0 for _ in range(N+1)]
li = [
[3, 10],
[5, 20],
[1, 10],
[1, 20],
[2, 15],
[4, 40],
[2, 200]
]

for i in range(N-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기면 상담을 하지 않는다.
    if i + li[i][0] > N:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        dp[i] = max(dp[i+1], li[i][1] + dp[i + li[i][0]])

print(dp[0])


