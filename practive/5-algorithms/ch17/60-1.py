# https://leetcode.com/problems/insertion-sort-list/description/
# 재미있는 문제다. 단 방향 리스트에서 이렇게 최적화를 한다라 성능이 아주 우수하다
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            cur = parent
        return cur.next
