"""
    2220. Minimum Bit Flips to Convert Number
    https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

    A bit flip of a number x is choosing a bit in the binary representation
    of x and flipping it from either 0 to 1 or 1 to 0.

        - For example, for x = 7, the binary representation is 111 and we may
        choose any bit (including any leading zeros not shown) and flip it. We
        can flip the first bit from the right to get 110, flip the second bit
        from the right to get 101, flip the fifth bit from the right
        (a leading zero) to get 10111, etc.

    Given two integers start and goal, return the minimum number of bit flips
    to convert start to goal.

"""


#! Approach 1: Brute Force
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start > 0 or goal > 0:
            # Increment count if the current bits differ
            if (start & 1) != (goal & 1):
                count += 1
            # Shift both numbers to the right to check the next bits
            start >>= 1
            goal >>= 1
        return count


#! Approach 2: Recursive Approach
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Base case: both numbers have been fully processed
        if start == 0 and goal == 0:
            return 0

        # Flip for the current least significant bit
        flip = 1 if (start & 1) != (goal & 1) else 0

        # Recurse for the next bits by right-shifting both numbers
        return flip + self.minBitFlips(start >> 1, goal >> 1)


#! Approach 3: XOR Rules
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR to find differing bits
        xor_result = start ^ goal
        count = 0
        # Count the number of 1s in xor_result (differing bits)
        while xor_result:
            count += xor_result & 1  # Increment if the last bit is 1
            xor_result >>= 1  # Shift right to process the next bit
        return count


#! Approach 4: Brian Kernighan’s Algorithm
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR to find differing bits
        xor_result = start ^ goal
        count = 0
        # Brian Kernighans algorithm to count 1s
        while xor_result:
            xor_result &= xor_result - 1  # Clear the lowest set bit
            count += 1
        return count
