"""
    979. Distribute Coins in Binary Tree
    https://leetcode.com/problems/distribute-coins-in-binary-tree/

    You are given the root of a binary tree with n nodes where each node in the tree has node.val coins.
        There are n coins in total throughout the whole tree.

    In one move, we may choose two adjacent nodes and move one coin from one node to another.
        A move may be from parent to child, or from child to parent.

    Return the minimum number of moves required to make every node have exactly one coin.

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # self.ans = 0
        # def dfs(root):
        #     if root is None:
        #         return 0
        #     # if root.left:
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     self.ans += abs(left) + abs(right)
        #     return root.val + left  + right -1

        # dfs(root)
        # return self.ans

        # -----------------------------------------------------

        # res = 0
        # def dfs(root):
        #     nonlocal res
        #     if root is None:
        #         return 0

        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     res += abs(left) + abs(right)
        #     return root.val + left + right - 1
        # dfs(root)
        # return res

        # -----------------------------------------------------

        self.moves = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.moves += abs(left) + abs(right)
            return node.val + left + right - 1

        dfs(root)
        return self.moves
