# https://leetcode.com/problems/perfect-squares/description/
# 라그랑주의 사각형 정리 문제, dp로는어떻게 풀 수 있지?
# four-square = 네 개의 제곱수의 합으로 나타낼 수 있는 수
from bisect import bisect_left
from cmath import sqrt


#DP 너무 느리다. 실픅 2060ms
def numSquares(n):
	bisect_left
	dp = [0] + [float('inf')]*n
	for i in range(1, n+1):
		dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
	return dp[n]

#BFS 빠르다. 최적화가 잘 되어있음. 실픅 148ms
def numSquares(self, n):
	squares = [i**2 for i in range(1, int(n**0.5)+1)]
	d, q, nq = 1, {n}, set()
	while q:
		for node in q:
			for square in squares:
				if node == square: return d
				if node < square: break
				nq.add(node-square)
		q, nq, d = nq, set(), d+1



#라그랑주 사각형 정리를 통한 풀이 실측 42ms
class Solution:
    def numSquares(self, n):
        if int(sqrt(n)) ** 2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j * j)) ** 2 == n - j * j: return 2

        while n % 4 == 0:
            n >>= 2
        if n % 8 == 7: return 4
        return 3