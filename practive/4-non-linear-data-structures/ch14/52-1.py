# https://leetcode.com/problems/range-sum-of-bst/
# 이건 쉽네 재귀로 접근하면 아주 우아한 코드를 만들 수 있는데 왜 연상이 잘 안될까?


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        return (root.val if L <= root.val <= R else 0) + \
               self.rangeSumBST(root.left, L, R) + \
               self.rangeSumBST(root.right, L, R)


