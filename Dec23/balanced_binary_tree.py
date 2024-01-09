# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         return (self.Height(root) >= 0)
#     def Height(self, root):
#         if root is None:  return 0
#         leftheight, rightheight = self.Height(root.left), self.Height(root.right)
#         if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
#         return max(leftheight, rightheight) + 1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Time Complexity: O(N), where N is the number of nodes in the tree. The algorithm traverses each node once in a post-order fashion, and for each node, constant time operations are performed.
        # Space Complexity: O(H), where H is the height of the tree. This is the maximum depth of the recursive call stack. In the worst case, when the tree is skewed, the space complexity approaches O(N), but for a balanced tree, it's O(log N).
        def checkBalance(node):
            # Base case: If the current node is None, it is balanced and has height 0
            if not node:
                return True, 0

            # Recursively check the balance of left and right subtrees
            # So, in the context of your solution, during the post-order traversal:

            # The algorithm first recursively checks the balance of the left subtree.
            # Then, it recursively checks the balance of the right subtree.
            # Finally, it calculates the height of the current node.

            left_balanced, left_height = checkBalance(node.left)
            right_balanced, right_height = checkBalance(node.right)

            # Calculate the height of the current node
            current_height = max(left_height, right_height) + 1

            # Check if the current node is balanced
            is_current_balanced = abs(left_height - right_height) <= 1

            # Return whether the current node and its subtrees are balanced,
            # along with the height of the current node
            return (
                is_current_balanced and left_balanced and right_balanced,
                current_height,
            )

        # Start the post-order traversal to check for balance
        is_balanced, _ = checkBalance(root)
        return is_balanced

    # def isBalanced(self, root: TreeNode) -> bool:
    #     def getDepth(node):
    #         if not node:
    #             return 0
    #         return 1 + max(getDepth(node.left), getDepth(node.right))

    #     if not root:
    #         return True
    #     return abs(getDepth(root.left) - getDepth(root.right)) <=1 and \
    #             self.isBalanced(root.left) and self.isBalanced(root.right)
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     # Helper function to calculate the height of a node
    #     def height(node):
    #         if not node:
    #             return 0
    #         left_height = height(node.left)
    #         right_height = height(node.right)
    #         return 1 + max(left_height, right_height)

    #     # Helper function to check if the tree is balanced at each node
    #     def is_balanced_helper(node):
    #         if not node:
    #             return True

    #         left_height = height(node.left)
    #         right_height = height(node.right)

    #         # Check if the difference in heights is greater than 1
    #         if abs(left_height - right_height) > 1:
    #             return False

    #         # Recursively check if the left and right subtrees are balanced
    #         return is_balanced_helper(node.left) and is_balanced_helper(node.right)

    #     return is_balanced_helper(root)
