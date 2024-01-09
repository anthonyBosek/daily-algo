"""
    938. Range Sum of BST
    https://leetcode.com/problems/range-sum-of-bst/

    Given the root node of a binary search tree and two integers low and high,
        return the sum of values of all nodes with a value in the inclusive
        range [low, high].
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# my solution
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0

        def sum_nodes(node):
            if low <= node.val <= high:
                self.sum += node.val
            if node.left:
                sum_nodes(node.left)
            if node.right:
                sum_nodes(node.right)

        sum_nodes(root)
        return self.sum


# copilot solution
# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
#         def dfs(root):
#             if root:
#                 if low <= root.val <= high:
#                     self.ans += root.val
#                 if low < root.val:
#                     dfs(root.left)
#                 if root.val < high:
#                     dfs(root.right)

#         self.ans = 0
#         dfs(root)
#         return self.ans
