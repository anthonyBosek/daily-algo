"""
    1609. Even Odd Tree
    https://leetcode.com/problems/even-odd-tree/

    A binary tree is named Even-Odd if it meets the following conditions:

        - The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, and so on.
        - For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
        - For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

    Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        pass
