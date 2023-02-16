# https://leetcode.com/problems/sliding-window-maximum/
# 1번으로는 안 풀림 2번으로 풀어보자
# 2번도 안 풀린다. 여기 정답이 있다.
# https://leetcode.com/problems/sliding-window-maximum/solutions/871317/clear-thinking-process-with-picture-brute-force-to-mono-deque-python-java-javascript/?languageTags=python
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))

        return r
