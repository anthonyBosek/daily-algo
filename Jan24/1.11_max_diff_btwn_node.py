"""
    1026. Maximum Difference Between Node and Ancestor
    https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

    Given the root of a binary tree, find the maximum value v for which there exist different
        nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

    A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        pass

    # copilot solution
    #     self.max_diff = 0
    #     self.dfs(root, root.val, root.val)
    #     return self.max_diff

    # def dfs(self, node, max_val, min_val):
    #     if not node:
    #         return
    #     self.max_diff = max(self.max_diff, abs(max_val - node.val), abs(min_val - node.val))
    #     max_val = max(max_val, node.val)
    #     min_val = min(min_val, node.val)
    #     self.dfs(node.left, max_val, min_val)
    #     self.dfs(node.right, max_val, min_val)
