"""
    2331. Evaluate Boolean Binary Tree
    https://leetcode.com/problems/evaluate-boolean-binary-tree/

    You are given the root of a full binary tree with the following properties:

        • Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
        • Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.

    The evaluation of a node is as follows:

        • If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
        • Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.

    Return the boolean result of evaluating the root node.

    A full binary tree is a binary tree where each node has either 0 or 2 children.

    A leaf node is a node that has zero children.

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def evaluateNode(node):
            # check if leaf
            if not node.right and not node.left:
                return bool(node.val)
            else:
                if node.val == 2:
                    return evaluateNode(node.right) or evaluateNode(node.left)
                elif node.val == 3:
                    return evaluateNode(node.right) and evaluateNode(node.left)

        return evaluateNode(root)

        # ? -----------------------------------------------------------------------
        #! ----- dfs solution -----
        # def dfs(node):
        #     if not node.left and not node.right:
        #         return node.val
        #     if node.val == 2:
        #         return dfs(node.left) or dfs(node.right)
        #     return dfs(node.left) and dfs(node.right)

        # return dfs(root)

        # ? -----------------------------------------------------------------------
        #! ----- recursive solution -----
        # if not root:
        #     return True

        # if root.val == 0:
        #     return False
        # elif root.val == 1:
        #     return True
        # elif root.val == 2:
        #     return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        # else:
        #     return self.evaluateTree(root.left) and self.evaluateTree(root.right)
