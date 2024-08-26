"""
    590. N-ary Tree Postorder Traversal
    https://leetcode.com/problems/n-ary-tree-postorder-traversal/

    Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

    Nary-Tree input serialization is represented in their level order traversal.
    Each group of children is separated by the null value (See examples)

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []
        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res


#! Approach 1: Recursive
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []
        if not root:
            return result
        self._traverse_postorder(root, result)
        return result

    def _traverse_postorder(
        self, current_node: "Node", postorder_list: List[int]
    ) -> None:
        if not current_node:
            return

        # First, visit all children
        for child_node in current_node.children:
            self._traverse_postorder(child_node, postorder_list)

        # Then, add the current node's value
        postorder_list.append(current_node.val)


#! Approach 2: Iterative (Explicit Reversal)
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []

        # If the root is None, return the empty list
        if root is None:
            return result

        node_stack = [root]

        # Traverse the tree using the stack
        while node_stack:
            current_node = node_stack.pop()
            result.append(current_node.val)
            # Push all the children of the current node to the stack
            for child in current_node.children:
                node_stack.append(child)

        # Reverse the result list to get the correct postorder traversal
        result.reverse()
        return result


#! Approach 3: Iterative (Two Stacks)
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []

        # If the root is None, return the empty list
        if root is None:
            return result

        node_stack = [root]  # Stack for traversal
        reverse_stack = []  # Stack to reverse the order

        # Traverse the tree using the node_stack
        while node_stack:
            current_node = node_stack.pop()
            reverse_stack.append(current_node)

            # Push all the children of the current node to node_stack
            for child in current_node.children:
                node_stack.append(child)

        # Pop nodes from reverse_stack and add their values to the result list
        while reverse_stack:
            current_node = reverse_stack.pop()
            result.append(current_node.val)

        return result


#! Approach 4: Iterative (Without Reverse)
class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []
        # If the root is None, return the empty list
        if root is None:
            return result

        node_stack = [(root, False)]

        while node_stack:
            current_node, is_visited = node_stack.pop()

            if is_visited:
                # If the node has been visited, add its value to the result
                result.append(current_node.val)
            else:
                # Mark the current node as visited and push it back to the stack
                node_stack.append((current_node, True))

                # Push all children to the stack in reverse order
                for child in reversed(current_node.children):
                    node_stack.append((child, False))

        return result
