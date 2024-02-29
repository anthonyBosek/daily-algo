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
        q = [root]
        is_odd = False
        while q:
            new_q = []
            prev = None
            for node in q:
                if is_odd:
                    if node.val % 2 or (prev and prev.val <= node.val):
                        return False
                else:
                    if not node.val % 2 or (prev and prev.val >= node.val):
                        return False
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                prev = node
            q = new_q
            is_odd = not is_odd
        return True

        # -------------------------------------------------------------

        # if not root:
        #     return False
        # queue = [root]
        # level = 0
        # while queue:
        #     prev = None
        #     for _ in range(len(queue)):
        #         node = queue.pop(0)
        #         if level % 2 == 0:
        #             if node.val % 2 == 0 or (prev and node.val <= prev):
        #                 return False
        #         else:
        #             if node.val % 2 != 0 or (prev and node.val >= prev):
        #                 return False
        #         prev = node.val
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1
        # return True
