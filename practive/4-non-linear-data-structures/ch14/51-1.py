# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# 에러가 났을 때 존재하지 않는 위치에서 Solution.py가 에러를 뱉으면? 무엇이 문제지?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root
