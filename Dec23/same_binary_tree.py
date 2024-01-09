# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Time Complexity: O(min(N, M)), where N and M are the number of nodes in the two trees. In the worst case, it would traverse the smaller tree.
        # Space Complexity: O(min(H1, H2)), where H1 and H2 are the heights of the two trees. This is the maximum depth of the recursive call stack.
        if p and q:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )
        return p is q

    # DFS with stack
    def isSameTree(self, p, q):
        # Time Complexity: O(min(N, M)), similar to the recursive approach, this is the max depth of the stack.
        # Space Complexity: O(min(H1, H2)), where H1 and H2 are the heights of the two trees. This is the maximum size of the stack.
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        return True
