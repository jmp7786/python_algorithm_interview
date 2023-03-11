# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# inorder, preorder, postorder 세개가 있을때 2개의 쌍은 3가지 경우가 존재한다. 다른 경우는 어떻게 BST를 구성하지?
# BST가 아니라도 2가지의 순회만 있다면 전부 복구 할 수 있는 게 아닐까? chat gpt에게 물어봐야겠다.
# 아니 배열이 inorder라고 하면 모든 트리를 복구 할 수 있는 것 아닌가?
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node
