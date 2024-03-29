import timeit
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 `sum` 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # `sum = 0-1 knapsack`인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            left, right = i+1, len(nums) - 1

            while left < right:
                target = [nums[i], nums[left], nums[right]]
                target.sort()
                compute = sum(target)

                if compute < 0:
                    left += 1

                elif compute > 0:
                    right -= 1
                else:
                    if target not in result:
                        result.append(target)
                    left+=1
        return result

result = Solution().threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])
print(result)
