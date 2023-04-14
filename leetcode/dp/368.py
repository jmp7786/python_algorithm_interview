# https://leetcode.com/problems/largest-divisible-subset/description/
'''
    단순히 for문으로는 풀 수 없는 문제다.
'''
from typing import List


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1:
            return nums
        nums.sort()
        dp = [(0, 0)] * n
        dp[0] = (1, 0)
        maxIndex, maxVal = 0, 1
        for i in range(1, n):
            dp[i] = max((dp[j][0] + 1, j) for j in range(i + 1) if nums[i] % nums[j] is 0)
            print(maxVal, dp[i])
            if dp[i][0] > maxVal:
                maxIndex, maxVal = i, dp[i][0]
        i, lds = maxIndex, [nums[maxIndex]]
        while i != dp[i][1]:
            i = dp[i][1]
            lds.append(nums[i])
        return lds

# ----------------------------------------------------------------------
# 아래는 내가 푼 문제 dp를 이용해야 풀 수 있다.
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        def check(path):
            print(path)
            ans = [path[0]]
            for i in range(1, len(path)):
                count = 0
                for ans_num in ans:
                    if ans_num % path[i] == 0 or path[i] % ans_num == 0:
                        count += 1
                if count == len(ans):
                    if path[i] not in ans:
                        ans.append(path[i])
            print(ans)
            return ans
        ans = [ check(nums[i:]) for i in range(n) ]
        return max(ans , key = len)