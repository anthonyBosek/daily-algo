"""
    1239. Maximum Length of a Concatenated String with Unique Characters
    https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

    Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

    Return the maximum possible length of s.

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # """
        # 1. use bit manipulation to check if the string has unique characters
        # 2. use backtracking to find all the possible combinations
        # 3. return the max length of the string
        # """

        # 1. use bit manipulation to check if the string has unique characters
        # def checkUnique(s: str) -> bool:
        #     # 1.1 use a 26-bit integer to represent the 26 characters
        #     # 1.2 use bit manipulation to check if the string has unique characters
        #     # 1.3 return True if the string has unique characters
        #     # 1.4 return False if the string has duplicate characters
        #     seen = 0
        #     for c in s:
        #         if seen & (1 << (ord(c) - ord("a"))):
        #             return False
        #         seen |= 1 << (ord(c) - ord("a"))
        #     return True

        # # 2. use backtracking to find all the possible combinations
        # # 2.1 use a helper function to find all the possible combinations
        # # 2.2 return the max length of the string
        # def helper(arr: List[str], index: int, path: str, res: List[str]) -> None:
        #     # 2.2.1 base case
        #     if index == len(arr):
        #         if checkUnique(path):
        #             res.append(path)
        #         return
        #     # 2.2.2 recursive case
        #     helper(arr, index + 1, path, res)
        #     helper(arr, index + 1, path + arr[index], res)

        # # 2.3 use a helper function to find all the possible combinations
        # # 2.4 return the max length of the string
        # res = []
        # helper(arr, 0, "", res)
        # return max([len(s) for s in res]) if res else 0

        # ---------------------------------------------------------------------
        # 0. Brute Force
        # Time O(2^n)
        # Space O(n)
        # def is_unique(s):
        #     return len(s) == len(set(s))
        # res = 0
        # for i in range(1 << len(arr)):
        #     tmp = []
        #     for j in range(len(arr)):
        #         if i & (1 << j):
        #             tmp.append(arr[j])
        #     if is_unique("".join(tmp)):
        #         res = max(res, len("".join(tmp)))
        # return res
        # 1. DFS
        # Time O(2^n)
        # Space O(n)
        def dfs(idx, path):
            if len(path) != len(set(path)):
                return
            self.res = max(self.res, len(path))
            for i in range(idx, len(arr)):
                dfs(i + 1, path + arr[i])

        self.res = 0
        dfs(0, "")
        return self.res

        # 2. Bitmask
        # Time O(2^n)
        # Space O(n)
        # dp = [set()]
        # for a in arr:
        #     if len(a) != len(set(a)):
        #         continue
        #     a = set(a)
        #     for c in dp[:]:
        #         if a & c:
        #             continue
        #         dp.append(a | c)
        # return max(len(a) for a in dp)

        # ---------------------------------------------------------------------
        # arr.sort(key=len)
        # max_len = 0
        # for i in range(len(arr)):
        #     if len(arr[i]) == len(set(arr[i])):
        #         for j in range(i):
        #             if len(arr[i] + arr[j]) == len(set(arr[i] + arr[j])):
        #                 arr.append(arr[i] + arr[j])
        #                 max_len = max(max_len, len(arr[i] + arr[j]))
        # return max_len
