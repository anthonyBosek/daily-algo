"""
    1239. Maximum Length of a Concatenated String with Unique Characters
    https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

    Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

    Return the maximum possible length of s.

    A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

"""


# class Solution:
# def maxLength(self, arr: List[str]) -> int:
def maxLength(arr) -> int:
    count = 0
    for i in range(len(arr)):
        # if count > len(arr[i]):
        temp = arr[i]
        test = 0
        for j in range(i + 1, len(arr)):
            if set(arr[i]).isdisjoint(set(arr[j])):
                test = len(arr[i] + arr[j])
                print("test", test)
            if set(temp).isdisjoint(set(arr[j])):
                temp += arr[j]
                if len(temp) > count:
                    count = len(temp)
                x = len(arr[i] + arr[j])
                print("temp", temp)
                print("x", x)
                if x > count:
                    count = x
            if test > count:
                count = test
            print(count)
        if len(arr[i]) > len(set(arr[i])):
            return 0
        elif len(arr[i]) > count:
            count = len(arr[i])
    return count


print("answer", maxLength(["a", "abc", "d", "de", "def"]))


# # ---------------------------------------------------------------------
# # 0. Brute Force
# # Time O(2^n)
# # Space O(n)
# # def is_unique(s):
# #     return len(s) == len(set(s))
# # res = 0
# # for i in range(1 << len(arr)):
# #     tmp = []
# #     for j in range(len(arr)):
# #         if i & (1 << j):
# #             tmp.append(arr[j])
# #     if is_unique("".join(tmp)):
# #         res = max(res, len("".join(tmp)))
# # return res
# # 1. DFS
# # Time O(2^n)
# # Space O(n)
# def dfs(idx, path):
#     if len(path) != len(set(path)):
#         return
#     self.res = max(self.res, len(path))
#     for i in range(idx, len(arr)):
#         dfs(i + 1, path + arr[i])

# self.res = 0
# dfs(0, "")
# return self.res

# # 2. Bitmask
# # Time O(2^n)
# # Space O(n)
# # dp = [set()]
# # for a in arr:
# #     if len(a) != len(set(a)):
# #         continue
# #     a = set(a)
# #     for c in dp[:]:
# #         if a & c:
# #             continue
# #         dp.append(a | c)
# # return max(len(a) for a in dp)

# # ---------------------------------------------------------------------
# # arr.sort(key=len)
# # max_len = 0
# # for i in range(len(arr)):
# #     if len(arr[i]) == len(set(arr[i])):
# #         for j in range(i):
# #             if len(arr[i] + arr[j]) == len(set(arr[i] + arr[j])):
# #                 arr.append(arr[i] + arr[j])
# #                 max_len = max(max_len, len(arr[i] + arr[j]))
# # return max_len
