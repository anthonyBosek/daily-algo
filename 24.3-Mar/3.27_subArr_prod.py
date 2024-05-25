"""
    713. Subarray Product Less Than K
    https://leetcode.com/problems/subarray-product-less-than-k/

    Given an array of integers nums and an integer k, return the number of contiguous subarrays where
        the product of all the elements in the subarray is strictly less than k.

"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        n = len(nums)

        curr_product = 1
        ans = 0
        left = 0
        for right in range(n):
            curr_product *= nums[right]
            while curr_product >= k:
                curr_product //= nums[left]
                left += 1

            ans += right - left + 1

        return ans

        # -----------------------------------------------------------

        # if k <= 1:
        #     return 0

        # n = len(nums)
        # left = 0
        # right = 0
        # prod = 1
        # count = 0

        # while right < n:
        #     prod *= nums[right]

        #     while prod >= k:
        #         prod /= nums[left]
        #         left += 1

        #     count += right - left + 1
        #     right += 1

        # return count

        # -----------------------------------------------------------

        # if k <= 1:
        #     return 0

        # count = 0
        # product = 1
        # left = 0

        # for right in range(len(nums)):
        #     product *= nums[right]

        #     while product >= k:
        #         product /= nums[left]
        #         left += 1

        #     count += right - left + 1

        # return count

        # -----------------------------------------------------------

        # if k <= 1:
        #     return 0

        # prod = 1
        # ans = left = 0

        # for right, val in enumerate(nums):
        #     prod *= val

        #     while prod >= k:
        #         prod /= nums[left]
        #         left += 1

        #     ans += right - left + 1

        # return ans
