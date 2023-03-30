# https://leetcode.com/problems/fruit-into-baskets/
from collections import Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        cnt = Counter()
        l = 0
        for r in range(len(fruits)):
            cnt[fruits[r]] += 1
            # 한칸씩 움직이기 때문에 while문으 사용하지 않아도 된다.
            if len(cnt) > 2:
                cnt[fruits[l]] -= 1
                if cnt[fruits[l]] == 0: cnt.pop(fruits[l])
                l += 1
            ans = max(ans, r - l + 1)
        return ans