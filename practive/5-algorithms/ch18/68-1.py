# 2번 풀이로 가시오
# 이 함수의 시간 복잡도는 어떻게 되는가?
# O(n^n-1/2)에 해당하는 함수를 생성해보시오
# 하나의 리스트에서 두 개의 인덱스를 핸들링한다? -> 투포인터
# 배열이 정렬되어 있다. -> 이진 탐색
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1  # 리턴 값 +1
