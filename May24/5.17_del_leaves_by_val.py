"""
    1325. Delete Leaves With a Given Value
    https://leetcode.com/problems/delete-leaves-with-a-given-value/

    Given a binary tree root and an integer target, delete all the leaf nodes with value target.

    Note that once you delete a leaf node with value target, if it's parent node becomes a leaf
        node and has the value target, it should also be deleted
        (you need to continue doing that until you can't).

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None

        return root

        # -----------------------------------------------------------------------------------------
        #! Recursive solution with helper func from leetcode

        # # recursive soln for root - if its child is a leaf node AND its child has target, delete
        # # go up
        # def helper(node):
        #     # first go down if necessary
        #     if not node:
        #         return

        #     helper(node.left)
        #     helper(node.right)
        #     # potentially delete left child
        #     # if node.val == target:
        #     # print(f'For node {node.val} we have left {node.left} and right {node.right}')
        #     if (
        #         node.left
        #         and not node.left.left
        #         and not node.left.right
        #         and node.left.val == target
        #     ):

        #         node.left = None
        #     # potentially delete right child
        #     if (
        #         node.right
        #         and not node.right.left
        #         and not node.right.right
        #         and node.right.val == target
        #     ):
        #         node.right = None

        # helper(root)
        # # we have an edge case here where root itself is a leaf and needs deletion
        # if root.val == target and not root.left and not root.right:
        #     return None
        # return root
