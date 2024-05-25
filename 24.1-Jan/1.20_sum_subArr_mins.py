"""
    907. Sum of Subarray Minimums
    https://leetcode.com/problems/sum-of-subarray-minimums/

    Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr.
    Since the answer may be large, return the answer modulo 109 + 7.

"""


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 1. Brute Force
        """
        T(n) = O(n)
        S(n) = O(n)
        """
        MOD = 10**9 + 7
        n = len(arr)
        left, right = [0] * n, [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        return sum((i - left[i]) * (right[i] - i) * arr[i] for i in range(n)) % MOD

        # 2. Stack
        # """
        # T(n) = O(n)
        # S(n) = O(n)
        # """
        # MOD = 10**9 + 7
        # n = len(arr)
        # stack = []
        # res = 0
        # for i in range(n):
        #     count = 1
        #     while stack and stack[-1][0] >= arr[i]:
        #         val, c = stack.pop()
        #         count += c
        #         res -= val * c
        #     stack.append((arr[i], count))
        #     res += arr[i] * count
        # return res % MOD

        # 3. DP
        # """
        # T(n) = O(n)
        # S(n) = O(n)
        # """
        # MOD = 10**9 + 7
        # n = len(arr)
        # left, right = [0] * n, [0] * n
        # stack = []
        # for i in range(n):
        #     while stack and arr[stack[-1]] > arr[i]:
        #         stack.pop()
        #     left[i] = stack[-1] if stack else -1
        #     stack.append(i)
        # stack = []
        # for i in range(n - 1, -1, -1):
        #     while stack and arr[stack[-1]] >= arr[i]:
        #         stack.pop()
        #     right[i] = stack[-1] if stack else n
        #     stack.append(i)
        # return sum((i - left[i]) * (right[i] - i) * arr[i] for i in range(n)) % MOD
