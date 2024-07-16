"""
    2096. Step-By-Step Directions From a Binary Tree Node to Another
    https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

    You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n.
    You are also given an integer startValue representing the value of the start node s, and a different integer
    destValue representing the value of the destination node t.

    Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path
    as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

        - 'L' means to go from a node to its left child node.
        - 'R' means to go from a node to its right child node.
        - 'U' means to go from a node to its parent node.

    Return the step-by-step directions of the shortest path from node s to node t.

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def find(node, val, path):
            if node.val == val:
                return True
            if node.left and find(node.left, val, path):
                path.append("L")
                return True
            if node.right and find(node.right, val, path):
                path.append("R")
                return True
            return False

        p1 = []
        p2 = []
        find(root, startValue, p1)
        find = find(root, destValue, p2)
        while p1 and p2 and p1[-1] == p2[-1]:
            p1.pop()
            p2.pop()
        return "U" * len(p1) + "".join(p2[::-1])


# ---------------------------------------------------------------------------------------------------------


#! Approach 1: BFS + DFS
class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        # Map to store parent nodes
        parent_map = {}

        # Find the start node and populate parent map
        start_node = self._find_start_node(root, startValue)
        self._populate_parent_map(root, parent_map)

        # Perform BFS to find the path
        q = deque([start_node])
        visited_nodes = set()
        # Key: next node, Value: <current node, direction>
        path_tracker = {}
        visited_nodes.add(start_node)

        while q:
            current_element = q.popleft()

            # If destination is reached, return the path
            if current_element.val == destValue:
                return self._backtrack_path(current_element, path_tracker)

            # Check and add parent node
            if current_element.val in parent_map:
                parent_node = parent_map[current_element.val]
                if parent_node not in visited_nodes:
                    q.append(parent_node)
                    path_tracker[parent_node] = (current_element, "U")
                    visited_nodes.add(parent_node)

            # Check and add left child
            if current_element.left and current_element.left not in visited_nodes:
                q.append(current_element.left)
                path_tracker[current_element.left] = (current_element, "L")
                visited_nodes.add(current_element.left)

            # Check and add right child
            if current_element.right and current_element.right not in visited_nodes:
                q.append(current_element.right)
                path_tracker[current_element.right] = (current_element, "R")
                visited_nodes.add(current_element.right)

        # This line should never be reached if the tree is valid
        return ""

    def _backtrack_path(self, node, path_tracker):
        path = []
        # Construct the path
        while node in path_tracker:
            # Add the directions in reverse order and move on to the previous node
            path.append(path_tracker[node][1])
            node = path_tracker[node][0]
        path.reverse()
        return "".join(path)

    def _populate_parent_map(self, node, parent_map):
        if not node:
            return

        # Add children to the map and recurse further
        if node.left:
            parent_map[node.left.val] = node
            self._populate_parent_map(node.left, parent_map)

        if node.right:
            parent_map[node.right.val] = node
            self._populate_parent_map(node.right, parent_map)

    def _find_start_node(self, node, start_value):
        if not node:
            return None

        if node.val == start_value:
            return node

        left_result = self._find_start_node(node.left, start_value)

        # If left subtree returns a node, it must be StartNode. Return it
        # Otherwise, return whatever is returned by right subtree.
        if left_result:
            return left_result
        return self._find_start_node(node.right, start_value)


# ---------------------------------------------------------------------------------------------------------


#! Approach 2: LCA + DFS
class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        # Find the Lowest Common Ancestor (LCA) of start and destination nodes
        lowest_common_ancestor = self._find_lowest_common_ancestor(
            root, startValue, destValue
        )

        path_to_start = []
        path_to_dest = []

        # Find paths from LCA to start and destination nodes
        self._find_path(lowest_common_ancestor, startValue, path_to_start)
        self._find_path(lowest_common_ancestor, destValue, path_to_dest)

        directions = []

        # Add "U" for each step to go up from start to LCA
        directions.extend("U" * len(path_to_start))

        # Append the path from LCA to destination
        directions.extend(path_to_dest)

        return "".join(directions)

    def _find_lowest_common_ancestor(
        self, node: TreeNode, value1: int, value2: int
    ) -> TreeNode:
        if node is None:
            return None

        if node.val == value1 or node.val == value2:
            return node

        left_lca = self._find_lowest_common_ancestor(node.left, value1, value2)
        right_lca = self._find_lowest_common_ancestor(node.right, value1, value2)

        if left_lca is None:
            return right_lca
        elif right_lca is None:
            return left_lca
        else:
            return node  # Both values found, this is the LCA

    def _find_path(self, node: TreeNode, target_value: int, path: List[str]) -> bool:
        if node is None:
            return False

        if node.val == target_value:
            return True

        # Try left subtree
        path.append("L")
        if self._find_path(node.left, target_value, path):
            return True
        path.pop()  # Remove last character

        # Try right subtree
        path.append("R")
        if self._find_path(node.right, target_value, path):
            return True
        path.pop()  # Remove last character

        return False


# ---------------------------------------------------------------------------------------------------------


#! Approach 3: LCA + DFS (Optimized)
class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        start_path = []
        dest_path = []

        # Find paths from root to start and destination nodes
        self._find_path(root, startValue, start_path)
        self._find_path(root, destValue, dest_path)

        directions = []
        common_path_length = 0

        # Find the length of the common path
        while (
            common_path_length < len(start_path)
            and common_path_length < len(dest_path)
            and start_path[common_path_length] == dest_path[common_path_length]
        ):
            common_path_length += 1

        # Add "U" for each step to go up from start to common ancestor
        directions.extend("U" * (len(start_path) - common_path_length))

        # Add directions from common ancestor to destination
        directions.extend(dest_path[common_path_length:])

        return "".join(directions)

    def _find_path(self, node: TreeNode, target: int, path: List[str]) -> bool:
        if node is None:
            return False

        if node.val == target:
            return True

        # Try left subtree
        path.append("L")
        if self._find_path(node.left, target, path):
            return True
        path.pop()  # Remove last character

        # Try right subtree
        path.append("R")
        if self._find_path(node.right, target, path):
            return True
        path.pop()  # Remove last character

        return False
