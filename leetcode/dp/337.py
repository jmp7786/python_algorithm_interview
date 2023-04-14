# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
          if not node:
            return [0,0]
          left = dfs(node.left)
          right = dfs(node.right)
          res = [0,0]
          res[0] = left[1] + right[1] + node.val
          res[1] =  max(left)+ max(right)
          return res
        return max(dfs(root))
# ----------------------------------------------------------------------
# 아래는 나의 코드 순회하는 방법이 잘못되었다. 마지막에 중복 노드가 발생하는 문제, 중간에 노드가 끊겨서 생기는 문제가 발생했다.
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # 순회하면서 전 단계의 값을 가져오는 것과 과 전전과 현재 값을 가져오는 것 중에서 큰 걸 반복한다.
        def dfs(node, moneys):
            print(moneys, not node)
            if not node:
                return moneys
            money = node.val
            if len(moneys) == 0:
                moneys.append(money)
            elif len(moneys) == 1:
                moneys.append(max(moneys[-1], money))
            else:
                moneys.append(max(moneys[-2] + money, moneys[-1]))
            left = dfs(node.left, moneys[:])
            right = dfs(node.right, moneys[:])

            return

        return dfs(root, [])

'''
public class Solution {
    public int rob(TreeNode root) {
        int[] num = dfs(root);
        return Math.max(num[0], num[1]);
    }
    private int[] dfs(TreeNode x) {
        if (x == null) return new int[2];
        int[] left = dfs(x.left);
        int[] right = dfs(x.right);
        int[] res = new int[2];
        res[0] = left[1] + right[1] + x.val;
        res[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return res;
    }
}
'''
