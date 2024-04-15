"""
    129. Sum Root to Leaf Numbers
    https://leetcode.com/problems/sum-root-to-leaf-numbers/

    You are given the root of a binary tree containing digits from 0 to 9 only.

    Each root-to-leaf path in the tree represents a number.

        - For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

    Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

    A leaf node is a node with no children.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# another solution...
# class Solution:
#     def _sum_numbers(self, root: Optional[TreeNode], cur_num: int):
#         if not root:
#             return 0
#         cur_num = cur_num * 10 + root.val
#         if root.left is None and root.right is None:
#             return cur_num
#         return self._sum_numbers(root.left, cur_num) + self._sum_numbers(root.right, cur_num)

#     def sumNumbers(self, root: Optional[TreeNode]) -> int:
#         return self._sum_numbers(root, 0)


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # ------ sample 1 ------
        ans = 0

        def dfs(node, path: str):
            nonlocal ans
            path = path + str(node.val)
            if not node.left and not node.right:
                ans += int(path)
            else:
                if node.left:
                    dfs(node.left, path)
                if node.right:
                    dfs(node.right, path)

        dfs(root, "")
        return ans

        # ------ sample 2 ------

        # all_nums = []

        # def dfs(node, curr_str):
        #     if not node:
        #         # all_nums.append(curr_str)
        #         return
        #     if not node.left and not node.right:
        #         all_nums.append(int(curr_str + str(node.val)))
        #         return
        #     curr_str += str(node.val)
        #     dfs(node.left, curr_str)
        #     dfs(node.right, curr_str)

        # dfs(root, "")
        # # print(all_nums)

        # return sum(all_nums)

        # ------ copilot ------

        # def dfs(node, num):
        #     if not node:
        #         return 0
        #     num = num * 10 + node.val
        #     if not node.left and not node.right:
        #         return num
        #     return dfs(node.left, num) + dfs(node.right, num)
        # return dfs(root, 0)
