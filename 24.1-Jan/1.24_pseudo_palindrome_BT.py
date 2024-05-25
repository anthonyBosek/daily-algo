"""
    1457. Pseudo-Palindromic Paths in a Binary Tree
    https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

    Given a binary tree where node values are digits from 1 to 9.
    A path in the binary tree is said to be pseudo-palindromic
    if at least one permutation of the node values in the path is a palindrome.

    Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            path ^= 1 << node.val
            if not node.left and not node.right:
                return 1 if path & (path - 1) == 0 else 0
            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)

        # ---------------------------------------------------------
        # def dfs(node, path):
        #     if not node:
        #         return 0
        #     path ^= 1 << node.val
        #     if not node.left and not node.right:
        #         return (path & (path - 1)) == 0
        #     return dfs(node.left, path) + dfs(node.right, path)

        # return dfs(root, 0)
