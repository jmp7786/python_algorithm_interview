# https://leetcode.com/problems/ugly-number-ii/description/
# 세상에 천재들은 많구나 또 한 수 배워간다. 아름다운 알고리즘이다.

class Solution:
    def nthUglyNumber(self, n):
        factors, k = [2,3,5], 3
        starts, nums = [0] * k, [1]
        for i in range(n-1):
            candidates = [factors[i]*nums[starts[i]] for i in range(k)]
            new_num = min(candidates)
            nums.append(new_num)
            starts = [starts[i] + (candidates[i] == new_num) for i in range(k)]
        return nums[-1]

print(True+ 1)


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1] * n
        numbers = [1] * len(primes)
        primes_n = len(primes)
        for i in range(1, n):
            print(dp, i)
            print([primes[i] ** numbers[i] for i in range(primes_n)], numbers)
            dp[i] = min([primes[i] ** numbers[i] for i in range(primes_n)])
            for j in range(primes_n-1, -1, -1):
                if primes[j] ** numbers[j]  == dp[i]:
                    numbers[j] += 1
                    break

        print(numbers, dp)

        return dp[-1]
