# https://leetcode.com/problems/longest-increasing-subsequence/
# 정렬되어있지 않아서 중간에 넘겨야 하는 값이 들어가면 어떻게 해야하지?
# DP를 이용해서 모든 상황을 기록할 수 있다.
from bisect import bisect_left
from typing import List

#DP
class Solution:  # 2516 ms, faster than 64.96%
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

#BS를 이용한 풀이, 아이이어가 굉장하다. 외우지는 말자.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)