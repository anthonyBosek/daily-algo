"""
    945. Minimum Increment to Make Array Unique
    https://leetcode.com/problems/minimum-increment-to-make-array-unique/

    You are given an integer array nums. In one move, you can pick an index i
    where 0 <= i < nums.length and increment nums[i] by 1.

    Return the minimum number of moves to make every value in nums unique.

    The test cases are generated so that the answer fits in a 32-bit integer.

"""


def minIncrementForUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    moves = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            moves += nums[i - 1] - nums[i] + 1
            nums[i] = nums[i - 1] + 1
    return moves

    # ----------------------------------------

    # dp = [0] * (max(nums) + 1)
    # for num in nums:
    #     dp[num] += 1

    # count = 0
    # for i in range(len(dp) - 1):
    #     if dp[i] > 1:
    #         count += dp[i] - 1
    #         dp[i + 1] += dp[i] - 1
    # count += dp[-1] * (dp[-1] - 1) // 2
    # return count

    # ----------------------------------------
    # --- editorial solution 1 ---
    # min_increments = 0
    # nums.sort()

    # for i in range(1, len(nums)):
    #     # Ensure each element is greater than its previous
    #     if nums[i] <= nums[i - 1]:
    #         # Add the required increment to minIncrements
    #         increment = nums[i - 1] + 1 - nums[i]
    #         min_increments += increment

    #         # Set the element to be greater than its previous
    #         nums[i] = nums[i - 1] + 1

    # return min_increments

    # ----------------------------------------
    # --- editorial solution 2 ---
    # n = len(nums)
    # max_val = max(nums)
    # min_increments = 0

    # # Create a frequencyCount array to store the frequency of each value in nums
    # frequency_count = [0] * (n + max_val + 1)

    # # Populate frequencyCount array with the frequency of each value in nums
    # for val in nums:
    #     frequency_count[val] += 1

    # # Iterate over the frequencyCount array to make all values unique
    # for i in range(len(frequency_count)):
    #     if frequency_count[i] <= 1:
    #         continue

    #     # Determine excess occurrences, carry them over to the next value,
    #     # ensure single occurrence for current value, and update min_increments.
    #     duplicates = frequency_count[i] - 1
    #     frequency_count[i + 1] += duplicates
    #     frequency_count[i] = 1
    #     min_increments += duplicates

    # return min_increments
