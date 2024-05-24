"""
    404. Sum of Left Leaves
    https://leetcode.com/problems/sum-of-left-leaves/

    Given the root of a binary tree, return the sum of all left leaves.

    A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # total = 0
        # stack = [(root, 0)]
        # while stack:
        #     root, pos = stack.pop()
        #     if pos and not root.left and not root.right:
        #         total += root.val
        #     if root.left:
        #         stack.append((root.left, 1))
        #     if root.right:
        #         stack.append((root.right, 0))

        # return total

        # ---------------------------------------------------------

        # if not root:
        #     return 0

        # def dfs(node, left):

        #     if not node:
        #         return 0

        #     if not node.left and not node.right:
        #         if left:
        #             return node.val
        #         else:
        #             return 0

        #     return dfs(node.left, True) + dfs(node.right, False)
        # return dfs(root.left, True) + dfs(root.right, False)

        # ---------------------------------------------------------

        if not root:
            return 0

        def isLeaf(node):
            return not node.left and not node.right

        def dfs(node, isLeft):
            if not node:
                return 0

            if isLeaf(node) and isLeft:
                return node.val

            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)
