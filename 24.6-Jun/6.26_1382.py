"""
    1382. Balance a Binary Search Tree
    https://leetcode.com/problems/balance-a-binary-search-tree/

    Given the root of a binary search tree, return a balanced binary search tree with the same node values.
    If there is more than one answer, return any of them.

    A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        pass
