"""
    872. Leaf-Similar Trees
    https://leetcode.com/problems/leaf-similar-trees/

    Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence. 
    Two binary trees are considered leaf-similar if their leaf value sequence is the same.
    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# my solution
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf_list(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return leaf_list(node.left) + leaf_list(node.right)

        return leaf_list(root1) == leaf_list(root2)


# copilot solution
# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         def get_leaves(node):
#             if not node:
#                 return []
#             if not node.left and not node.right:
#                 return [node.val]
#             return get_leaves(node.left) + get_leaves(node.right)

#         return get_leaves(root1) == get_leaves(root2)
