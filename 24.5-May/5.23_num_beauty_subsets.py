"""
    2597. The Number of Beautiful Subsets
    https://leetcode.com/problems/the-number-of-beautiful-subsets/

    You are given an array nums of positive integers and a positive integer k.

    A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

    Return the number of non-empty beautiful subsets of the array nums.

    A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums.
        Two subsets are different if and only if the chosen indices to delete are different.

"""

from typing import List
from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        tot_count = 1
        freq_map = defaultdict(dict)

        # Calculate frequencies based on remainder
        for num in nums:
            remainder = num % k
            freq_map[remainder][num] = freq_map[remainder].get(num, 0) + 1

        # Iterate through each remainder group
        for fr in freq_map.values():
            n = len(fr)
            curr_count = 1
            next1 = 1
            next2 = 0
            subsets = sorted(fr.items())

            # Calculate counts for each subset starting from the second last
            for i in range(n - 1, -1, -1):
                # Count of subsets skipping the current subset
                skip = next1

                # Count of subsets including the current subset
                take = 2 ** subsets[i][1] - 1

                # If next number has a 'difference', calculate subsets; otherwise, move to next
                if i + 1 < n and subsets[i + 1][0] - subsets[i][0] == k:
                    take *= next2
                else:
                    take *= next1

                # Store the current total count for the current subset
                curr_count = skip + take
                next2, next1 = next1, curr_count

            tot_count *= curr_count

        return tot_count - 1

        # ---------------------------------------------------------------------------------------

        # def sol(nums, k):
        #     """
        #     must not contain diff == k

        #     which means elems with diff k are mutex in a subset, once chosen a num, the others cannot be chosen

        #     2: [4]
        #     4: [2, 6]
        #     6: [4]

        #     """
        #     nums.sort()
        #     n = len(nums)
        #     num_set = set(nums)
        #     mutex_dict = defaultdict(set)

        #     for num in nums:
        #         if num - k in num_set:
        #             mutex_dict[num].add(num - k)
        #         if num + k in num_set:
        #             mutex_dict[num].add(num + k)

        #     # print(mutex_dict)

        #     # start from the first number, do backtrack, and maintain a forbidden set
        #     ans = 0
        #     def backtrack(start, path, forbid_set):
        #         nonlocal ans
        #         if start == n: # reached oob
        #             if path:
        #                 ans += 1
        #             return
        #         # each number has two options
        #         # no pick
        #         backtrack(start + 1, path, forbid_set)

        #         # pick
        #         if nums[start] not in forbid_set:
        #             path.append(nums[start])
        #             new_forbid_set = forbid_set.union(mutex_dict[nums[start]])
        #             backtrack(start + 1, path, new_forbid_set)
        #             path.pop()
        #     backtrack(0, [], set())
        #     return ans
        # return sol(nums, k)

        # ----------------------------------------------------------------------------------

        # """
        # # nums = [2,4,6]
        # # k = 2
        # # [], [2], [4], [6], [2, 4], [2, 6], [4, 6], [2, 4, 6]
        # # [2], [4], [6], [2, 6] -> 4 ans
        # # SOLUTION
        # # num - k or n + k
        # """

        # count = 0
        # lenNums = len(nums)

        # def explore(index):
        #     nonlocal count
        #     if lenNums == index:
        #         count += 1
        #         return

        #     num = nums[index]

        #     if num - k not in visited and num + k not in visited:
        #         visited[num] += 1
        #         explore(index + 1)
        #         visited[num] -= 1
        #         if visited[num] == 0:
        #             del visited[num]

        #     explore(index + 1)

        # visited = defaultdict(int)
        # explore(0)
        # return count - 1
