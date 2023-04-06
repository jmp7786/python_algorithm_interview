# https://leetcode.com/problems/unique-binary-search-trees-ii/
# 96번 문제는 같은 경우의 경우의 수를 찾는 문제이고 이건 경로를 다 찾는 문제이다.
# BF로 풀어도 된다. -> 제약 조건이 매우 작게 되어있음
# 문제에서 TreeNode를 주는지 확인해야 한다. return을 배열로 하는 건지 node로 하는 건지 알 수 있음
# 문제를 제대로 알 수 있다. BFS를 통해서 TreeNode를 만드는 일은 그리 어렵지 않다. 
from functools import lru_cache
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def dfs(left, right):
            if left > right: return [None]
            if left == right: return [TreeNode(left)]
            ans = []
            for root in range(left, right + 1):
                leftNodes = dfs(left, root - 1)
                rightNodes = dfs(root + 1, right)
                for leftNode in leftNodes:
                    for rightNode in rightNodes:
                        rootNode = TreeNode(root, leftNode, rightNode)
                        ans.append(rootNode)
            return ans

        return dfs(1, n)