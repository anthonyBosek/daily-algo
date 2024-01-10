"""
    2385. Amount of Time for Binary Tree to Be Infected
    https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

    Given the root of a binary tree and an integer k, return the number of nodes in the
        tree that are at most k distance from the infected node.
    You can assume that the given root is always infected, and that k is always positive.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # my solution

        # copilot solution
        def infect(node, time):
            if not node:
                return
            if time == 0:
                node.infected = True
            infect(node.left, time - 1)
            infect(node.right, time - 1)

        def count_infected(node):
            if not node:
                return 0
            if node.infected:
                return 1 + count_infected(node.left) + count_infected(node.right)
            return count_infected(node.left) + count_infected(node.right)

        infect(root, start)
        return count_infected(root)
