# https://leetcode.com/problems/task-scheduler/

import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            print('counter1',counter)
            # +1 을 붙여줌으로서 idle인 상태까지 감안해서 알고리즘을 구현할 수 있다. p.598
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result

result = Solution().leastInterval(["A","A","A","B","B","B","C"], 2)
print(result)

result = Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 1)
print(result)
