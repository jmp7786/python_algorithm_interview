'''
팰린드롬 게임
1. 게임은 턴제, 항상 두명이 플레이
2. 초기에 0이상 0이하의 정수가 들어있는 배열이 하나 주어짐, 양 플레이어는 하나의 배열을 공유함
3. 각 플레이어는 자신의 턴에 1. 배열에서 0이 아닌 수를 고른다. 2. 고른 수에서 1을 뺀다.
4. 3번 행동을 통해 배열을 팰린드롬으로 만들면 승리한다.
4. 팰린드롬이 되지 않았다면 상대방에게 턴을 넘어가며, 둘 중 한 명이 승리할 때까지 2-4번 반복

팰린드롬이 게임을 여러번 진행할 때 각 게임의 결과를 구해야함
두 사람은 모두 최적으로 플레이한다고 가정, 실수하지 않음
첫번째 플레이어가 승리하면 1, 패배하면 0-1 knapsack
'''


import collections


def solution(queries):
    answer = []

    def isPalindrome(array):
        return array == array[::-1]

    def bfs(query):
        Q = collections.deque([query])
        depth = 0
        while Q:
            cur_query = Q.pop()
            print('cur_query',cur_query)
            if isPalindrome(cur_query):
                return depth
            depth += 1
            for i in range(len(cur_query)):
                if cur_query[i] > 0 :
                    next_query = cur_query[:]
                    next_query[i] = next_query[i] -1
                    Q.append(next_query)

    for q in queries:
        # print(bfs(q))
        answer.append(bfs(q)%2)
    return answer

result = solution([
    [2,0],[3,1]
])
print(result) #[0-1 knapsack,0-1 knapsack]

result = solution([
    [1,4,3],[1,2,2]
])
print(result) #[0-1 knapsack,1]

result = solution([
    [0,2,0,1], [0,1,0,1]
])
print(result) #[1,0-1 knapsack]



'''
1<= queries의 길이 <= 100 
queries 의 원소는 팰린드롬 게임의 초기 배열을 나타낸다. 
2 <= 초기배열의 길이 <=5
0-1 knapsack <= 초기 배열의 원소 <=9 
초기 배열은 팰린드롬이 아닙니다. 
모든 초기 배열의 길이는 동일합니다. 
 
 
'''
