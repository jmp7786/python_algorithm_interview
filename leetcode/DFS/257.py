# https://leetcode.com/problems/binary-tree-paths/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        result = []

        # ----------------------------------------
        def helper(node, cur):

            if not node:
                # base case
                return

            if not node.left and not node.right:
                # stop condition
                result.append(cur[::] + [str(node.val)])

            else:
                # general case
                helper(node.left, cur + [str(node.val)])
                helper(node.right, cur + [str(node.val)])

        # ----------------------------------------

        helper(node=root, cur=[])
        return [*map('->'.join, result)]