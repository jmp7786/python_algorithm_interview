# https://leetcode.com/problems/task-scheduler/
import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        result = 0
        while True:
            sub_count = 0
            for task, _ in counts.most_common(n + 1):
                sub_count += 1
                result += 1

                counts.subtract(task)
                # counts의 0 이하 목록 삭제
                counts += collections.Counter()
            if not counts:
                break
            result += n - sub_count + 1

        return result

