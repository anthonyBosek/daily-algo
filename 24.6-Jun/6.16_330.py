"""
    330. Patching Array
    https://leetcode.com/problems/patching-array/

    Given a sorted integer array nums and an integer n, add/patch elements to the array such that
    any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

    Return the minimum number of patches required.

"""

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        upper, cost = 0, 0
        i = 0
        while upper < n:
            if i < len(nums) and nums[i] <= upper + 1:
                upper += nums[i]
                i += 1
            else:
                cost += 1
                upper += upper + 1
        return cost

        #! ---------------------------------------------------------

        # patches = 0
        # i = 0
        # miss = 1
        # while miss <= n:
        #     if i < len(nums) and nums[i] <= miss:
        #         miss += nums[i]
        #         i += 1
        #     else:
        #         miss += miss
        #         patches += 1
        # return patches

        #! ---------------------------------------------------------

        # ans = 0
        # i = 0  #? nums' index
        # miss = 1  #? the minimum sum in [1, n] we might miss

        # while miss <= n:
        #     if i < len(nums) and nums[i] <= miss:
        #         miss += nums[i]
        #         i += 1
        #     else:
        #         #? Greedily add `miss` itself to increase the range from
        #         #? [1, miss) to [1, 2 * miss).
        #         miss += miss
        #         ans += 1

        # return ans

        #! ---------------------------------------------------------

        # #? this is the first number that can't be built
        # #? by the numbers in the array so far
        # next_missing_sum = 1
        # i = 0
        # n_patches = 0
        # #? when the next missing sum hits n, we will be able to build
        # #? all numbers between 1 and n.
        # while next_missing_sum <= n:
        #     #? the next missing sum is larger than the current number
        #     #? which means we can build the current number
        #     if i < len(nums) and nums[i] <= next_missing_sum:
        #         #? now we can build up to a larger number by including nums[i]
        #         #? we can already build all numbers up through next_missing_sum
        #         #? now we can build to next_missing_sum + nums[i]
        #         next_missing_sum += nums[i]
        #         i += 1
        #     #? cannot build the next_missing_sum, which means we need to patch
        #     #? it in, but if we patch it in, we can now build up to (but not
        #     #? including) 2 * next_missing_sum, since we could build everything
        #     #? up through next_missing_sum
        #     #? if we have exhausted nums, then we just have to keep adding
        #     #? numbers to the end
        #     else:
        #         next_missing_sum += next_missing_sum
        #         n_patches += 1
        # return n_patches
