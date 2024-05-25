"""
    988. Smallest String Starting From Leaf
    https://leetcode.com/problems/smallest-string-starting-from-leaf/

    You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

    Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

    As a reminder, any shorter prefix of a string is lexicographically smaller.

        - For example, "ab" is lexicographically smaller than "aba".

    A leaf of a node is a node that has no children.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, cur):
            if not node:
                return ""
            cur = chr(ord("a") + node.val) + cur
            if not node.left and not node.right:
                return cur
            if not node.right:
                return dfs(node.left, cur)
            if not node.left:
                return dfs(node.right, cur)
            return min(dfs(node.left, cur), dfs(node.right, cur))

        return dfs(root, "")

        # -------------------------------------------------------------------

        # ans = []

        # def dfs(node, ds):
        #     if not node:
        #         return
        #     ds.append(chr(97 + node.val))

        #     if not node.left and not node.right:
        #         ans.append("".join(ds[::-1]))
        #         ds.pop()
        #         return
        #     dfs(node.left, ds)
        #     dfs(node.right, ds)
        #     ds.pop()

        # dfs(root, [])
        # ans.sort()
        # return ans[0]

        # -------------------------------------------------------------------

        # def dfs(node, path):
        #     if not node:
        #         return
        #     path.append(chr(node.val + ord("a")))
        #     if not node.left and not node.right:
        #         self.ans = min(self.ans, "".join(path[::-1]))
        #     dfs(node.left, path)
        #     dfs(node.right, path)
        #     path.pop()

        # self.ans = "~"
        # dfs(root, [])
        # return self.ans
