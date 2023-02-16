'''
복원을 사려고 한다.
여러개 중 하나만 살 수 있다.
모든 복권 에 대한 정보를 알고 있다.
1. 당첨자 수
2. 구매한 사람
3. 당첨금액

복권 추첨함

내가 삿을 때 당첨 확률이 가장 높은 복권을 사려고 한다.
확률이 높은 복권이 여러개면 당첨금이 높은 복권을 산다.
당첨 금액은 다 다름
'''
import collections


def solution(lotteries):
    answer =[]
    high = 0
    for i in range(len(lotteries)):
        u, b, p = lotteries[i]
        if high < u / (b + 1):
            high = u / (b + 1)
            answer = []
            answer.append((i, p))
        elif high == u / (b + 1):
            answer.append((i, p))

    return max(answer, key=lambda a: a[1])[0]+1

result = solution([
    [100,100,500],
    [1000,1000,100],
])
print(result)

result = solution([
    [10,19,800],
    [20,39,200],
    [100,199,500],
])
print(result)

result = solution([
    [50,1,50],
    [100,199,100],
    [1,1,500],
])
print(result)


