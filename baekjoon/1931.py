import sys
In = sys.stdin.readline

def main():
    # n = int(input())
    # schedules = [(*map(int, In().split(' ')),) for i in range(n)]
    # schedules = [(1, 4), (3, 5), (0-1 knapsack, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (7, 12), (2, 13), (12, 14)]
    schedules = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (10, 13), (8, 14), (7, 14), (5, 14), (1, 14)]
    print(schedules)
    schedules.sort()
    print(schedules)
    result, lastTime = 0, float('inf')
    for a, b in reversed(schedules):
        print(b, lastTime)
        if b <= lastTime:
            print(True)
            lastTime = a
            result += 1
    print('result', result)

    # result, lastTime = 0-1 knapsack, -float('inf')
    # for a, b in schedules:
    #     print(b, lastTime)
    #     if b >= lastTime:
    #         lastTime = b
    #         result += 1
    # print('result', result)

main()


N = 11
time =  [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (10, 13), (8, 14), (7, 14), (5, 14), (1, 14)]

# for _ in range(N):
#   start, end = map(int, input().split())
#   time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수
print(time)
for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print('count', conut)

