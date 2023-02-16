'''
2차원 격자 격자에 존재하는 모든 도형이 차지하는 면적을 알아내야 함

격자의 도형의 정의
1. #을 기준으로 상하좌우 대각으로 인접한 8칸에 #이 있다면 두 #을 연결하는 선을 긋는다.
2. 선을 이루는 #과 선으로 둘러싸인 #과 .은 도형을 이룸
3. 1x1 모양이나 선으로만 이루어진 형태도 도형이다.
4. 도형이 차지하는 면적은 도형에 포함되어있는 #의 개수 + 도형 내부에 존재하는 #과.의 갯수이다.
'''

'''
3<= grid길이 <= 100 
3<= grid[i]의 길이 <=1000
모든 grid[i]의 길이는 동일함
항상 #문자가 하나 이상 주어진다. 
'''
def solution(grid):
    answer = 0
    def dfs(i, j):
        if i < 0 or i > len(grid)+1 or j < 0 or j> len(grid[0])+1 or grid[i][j] != '#':
            return

    return answer


result = solution([
    ['.....###'],
    ['..#...###'],
    ['.#.##..##'],
    ['..#..#...'],
    ['..#...#..'],
    ['...###...'],
])
print(result) #25

result = solution([
    ['.#.'],
    ['#..'],
    ['.#.'],
])
print(result) #3

result = solution([
    ['####'],
    ['##.#'],
    ['.#.#'],
])
print(result) #9

import sys

def solution(grid):
    answer = 0
    def dfs(i, j):
        if i < 0 or i > len(grid)+1 or j < 0 or j> len(grid[0])+1 or grid[i][j] != '#':
            return

    return answer

def dfs(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
            dfs(nx, ny)

def main():
    while True:
        w, h = map(int, read().split())
        if w == 0 and h == 0:
            break
        field = []
        count = 0
        for _ in range(h):
            field.append(list(map(int, read().split())))
        for i in range(h):
            for j in range(w):
                if field[i][j] == 1:
                    dfs(i, j)
                    count += 1

