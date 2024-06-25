"""
    1038. Binary Search Tree to Greater Sum Tree
    https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

    Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

    As a reminder, a binary search tree is a tree that satisfies these constraints:

        • The left subtree of a node contains only nodes with keys less than the node's key.

        • The right subtree of a node contains only nodes with keys greater than the node's key.

        • Both the left and right subtrees must also be binary search trees.


    ***Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#! Approach 1: In-order Traversal (Brute-Force)
class Solution:
    def bstToGst(self, root):
        # Store the inorder traversal in an array.
        self.inorder_traversal = []
        self.inorder(root)

        # Reverse the array to get descending order.
        self.inorder_traversal.reverse()

        # Modify the values in the tree.
        self.replace_values(root)

        return root

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.inorder_traversal.append(root.val)
        self.inorder(root.right)

    # Function to modify the values in the tree.
    def replace_values(self, root):
        if root is None:
            return
        self.replace_values(root.left)
        self.replace_values(root.right)

        # Replace node with values greater than the current value.
        node_sum = 0
        for i in self.inorder_traversal:
            if i > root.val:
                node_sum += i
            else:
                break

        root.val += node_sum


#! Approach 2: Reverse In-order Traversal
class Solution:
    def bstToGst(self, root):
        node_sum = [0]  # Using a list to emulate a mutable integer reference
        self.bst_to_gst_helper(root, node_sum)
        return root

    def bst_to_gst_helper(self, root, node_sum):
        # If root is null, make no changes.
        if root is None:
            return

        self.bst_to_gst_helper(root.right, node_sum)
        node_sum[0] += root.val
        # Update the value of root.
        root.val = node_sum[0]
        self.bst_to_gst_helper(root.left, node_sum)


#! Approach 3: Iterative Reverse In-order Traversal
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_sum = 0
        st = []
        node = root

        while st or node is not None:

            while node is not None:
                st.append(node)
                node = node.right
            # Store the top value of stack in node and pop it.
            node = st.pop()

            # Update value of node.
            node_sum += node.val
            node.val = node_sum

            # Move to the left child of node.
            node = node.left
        return root


#! Approach 4: Morris Traversal
class Solution(object):
    def bstToGst(self, root):
        # Get the node with the smallest value greater than this one.
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                succ = get_successor(node)
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root
