"""
    2149. Rearrange Array Elements by Sign
    https://binarysearch.com/problems/Rearrange-Array-Elements-by-Sign

    You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

    You should rearrange the elements of nums such that the modified array follows the given conditions:

        1. Every consecutive pair of integers have opposite signs.
        2. For all integers with the same sign, the order in which they were present in nums is preserved.
        3. The rearranged array begins with a positive integer.

    Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # ------ my solution ------
        # pos = []
        # neg = []
        # solution = []

        # for num in nums:
        #     if num > 0:
        #         pos.append(num)
        #     else:
        #         neg.append(num)

        # for i in range(len(pos)):
        #     solution.append(pos[i])
        #     solution.append(neg[i])

        # return solution

        # --------------------------------------------------

        pos, neg = [], []

        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        nums[0 : len(pos) * 2 : 2] = pos
        nums[1 : len(neg) * 2 : 2] = neg

        return nums
