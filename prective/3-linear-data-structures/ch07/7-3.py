# https://leetcode.com/problems/two-sum/
import timeit
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if target-num in num_map:
                return [num_map[target-num], i]
            num_map[num] = i

if __name__ == '__main__':
    print(timeit.timeit("print(Solution().twoSum([1,2,2,3,7,9], 12))",
                                setup="from __main__ import Solution", number=1))





