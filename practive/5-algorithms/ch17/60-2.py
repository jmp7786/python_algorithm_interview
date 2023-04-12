# https://leetcode.com/problems/insertion-sort-list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 초기값 변경
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            #이거 순서를 지켜야 된다고??? 내가 잘못이해하고 있는 게 있나보네
            cur.next, head.next, head = head, cur.next, head.next

            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
            if head and cur.val > head.val:
                cur = parent
        return parent.next

'''
이 질문에서 제시된 코드는 연결 리스트에 대한 삽입 정렬 알고리즘을 구현한 것입니다. 코드에서 사용된 다중 할당 구문 cur.next, head.next, head = head, cur.next, head.next은 삽입 정렬 과정 중에 노드들의 연결 구조를 바꾸는데 사용되고 있습니다. 이 구문의 순서를 변경하면 연결 리스트의 구조가 올바르게 변경되지 않아 정렬 결과가 올바르지 않게 됩니다.

원래 코드에서는 다음과 같은 순서로 동작합니다.

cur.next에 현재 head를 연결합니다.
head.next를 cur.next (원래의 cur.next 노드)로 설정합니다.
head를 다음 노드로 이동시킵니다.

이렇게 하면 원래의 cur.next 노드가 head 노드 뒤에 올바르게 연결됩니다.

하지만 이 순서를 변경하면, 변수들이 참조하는 노드의 연결 관계가 꼬이게 되어 정렬 결과가 올바르지 않게 됩니다. 예를 들어, head.next, cur.next, head = head, cur.next, head.next와 같이 순서를 변경하면 다음과 같은 문제가 발생합니다.

head.next에 현재 head를 연결합니다. 이로 인해 head 노드가 자기 자신을 참조하게 되어 사실상 리스트가 끊기게 됩니다.
cur.next에 원래 cur.next 노드를 연결합니다. 이 경우 변경이 없습니다.
head를 다음 노드로 이동시킵니다. 그러나 head.next는 이미 1번 과정에서 head 노드 자체로 설정되었기 때문에, head는 자기 자신을 가리키게 되어 무한 루프에 빠지게 됩니다.

이처럼 순서를 변경하면 연결 리스트의 구조가 올바르게 변경되지 않기 때문에 정렬 결과가 올바르지 않게 됩니다. 따라서 원래의 순서인 cur.next, head.next, head = head, cur.next, head.next를 유지해야 올바른 정렬 결과를 얻을 수 있습니다.
'''