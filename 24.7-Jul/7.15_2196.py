"""
    2196. Create Binary Tree From Descriptions
    https://leetcode.com/problems/create-binary-tree-from-descriptions/

    You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates
    that parenti is the parent of childi in a binary tree of unique values. Furthermore,

        • If isLefti == 1, then childi is the left child of parenti.
        • If isLefti == 0, then childi is the right child of parenti.

    Construct the binary tree described by descriptions and return its root.

    The test cases will be generated such that the binary tree is valid.

"""

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        child = set()
        for p, c, l in descriptions:
            child.add(c)
            if p in d:
                p = d[p]
            else:
                d[p] = TreeNode(p)
                p = d[p]
            if c in d:
                c = d[c]
            else:
                d[c] = TreeNode(c)
                c = d[c]
            if l:
                p.left = c
            else:
                p.right = c

        for p, _, _ in descriptions:
            if p not in child:
                return d[p]

        return None


#! Approach 1: Convert to Graph with Breadth First Search
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Sets to track unique children and parents
        children = set()
        parents = set()
        # Dictionary to store parent to children relationships
        parentToChildren = {}

        # Build graph from parent to child, and add nodes to sets
        for d in descriptions:
            parent, child, isLeft = d
            parents.add(parent)
            parents.add(child)
            children.add(child)
            if parent not in parentToChildren:
                parentToChildren[parent] = []
            parentToChildren[parent].append((child, isLeft))

        # Find the root node by checking which node is
        # in parents but not in children
        for parent in parents.copy():
            if parent in children:
                parents.remove(parent)

        root = TreeNode(next(iter(parents)))

        # Starting from root, use BFS to construct binary tree
        queue = deque([root])

        while queue:
            parent = queue.popleft()
            # Iterate over children of current parent
            for childValue, isLeft in parentToChildren.get(parent.val, []):
                child = TreeNode(childValue)
                queue.append(child)
                # Attach child node to its parent based on isLeft flag
                if isLeft == 1:
                    parent.left = child
                else:
                    parent.right = child

        return root


#! Approach 2: Convert to Graph with Depth First Search
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Step 1: Organize data
        parent_to_children = {}
        all_nodes = set()
        children = set()

        for parent, child, is_left in descriptions:
            # Store child information under parent node
            if parent not in parent_to_children:
                parent_to_children[parent] = []
            parent_to_children[parent].append((child, is_left))
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)

        # Step 2: Find the root
        root_val = (all_nodes - children).pop()

        # Step 3 & 4: Build the tree using DFS
        def _dfs(val):
            # Create new TreeNode for current value
            node = TreeNode(val)

            # If current node has children, recursively build them
            if val in parent_to_children:
                for child, is_left in parent_to_children[val]:
                    # Attach child node based on is_left flag
                    if is_left:
                        node.left = _dfs(child)
                    else:
                        node.right = _dfs(child)
            return node

        return _dfs(root_val)


#! Approach 3: Constructing Tree From Directly Map and TreeNode Object
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Maps values to TreeNode pointers
        node_map = {}

        # Stores values which are children in the descriptions
        children = set()

        # Iterate through description to create nodes and set up tree structure
        for description in descriptions:
            # Extract parent value, child value, and whether
            # it is a left child (1) or right child (0)
            parent_value = description[0]
            child_value = description[1]
            is_left = bool(description[2])

            # Create parent and child nodes if not already created
            if parent_value not in node_map:
                node_map[parent_value] = TreeNode(parent_value)
            if child_value not in node_map:
                node_map[child_value] = TreeNode(child_value)

            # Attach child node to parent's left or right branch
            if is_left:
                node_map[parent_value].left = node_map[child_value]
            else:
                node_map[parent_value].right = node_map[child_value]

            # Mark child as a child in the set
            children.add(child_value)

        # Find and return the root node
        for node in node_map.values():
            if node.val not in children:
                return node  # Root node found

        return None  # Should not occur according to problem statement
