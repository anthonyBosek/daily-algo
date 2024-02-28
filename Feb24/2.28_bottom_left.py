"""
    513. Find Bottom Left Tree Value
    https://leetcode.com/problems/find-bottom-left-tree-value/

    Given the root of a binary tree, return the leftmost value in the last row of the tree.

"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left = root
        q = deque([root])

        while q:
            rowLen = len(q)
            for i in range(rowLen):
                n = q.popleft()
                if n:
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                    if i == 0:
                        left = n
        return left.val

        # ---------------------------------------------------------

        # if root is None:
        #     return None

        # queue = [root]
        # while queue:
        #     size = len(queue)
        #     for i in range(size):
        #         node = queue.pop(0)
        #         if i == 0:
        #             leftmost = node.val
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return leftmost

        # ---------------------------------------------------------

        # queue = [root]
        # while queue:
        #     node = queue.pop(0)
        #     if node.right:
        #         queue.append(node.right)
        #     if node.left:
        #         queue.append(node.left)
        # return node.val
