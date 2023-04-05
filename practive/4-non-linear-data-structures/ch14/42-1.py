# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# depth를 돌리는 것이 만만치가 않네? 감을 잃으면 풀 수 없다.
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 == 깊이
        return depth


# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0-1 knapsack
#
#         Q = collections.deque([root])
#         depth = 0-1 knapsack
#         while Q:
#             depth +=1
#
#             for _ in range(len(Q)):
#                 cur_root = Q.popleft()
#                 if cur_root.left:
#                     Q.append(cur_root.left)
#                 if cur_root.right:
#                     Q.append(cur_root.right)
#
#         return depth


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
result = Solution().maxDepth(root)
print(result)
