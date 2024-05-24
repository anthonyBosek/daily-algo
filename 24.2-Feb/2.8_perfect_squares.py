"""
    279. Perfect Squares
    https://leetcode.com/problems/perfect-squares/

    Given an integer n, return the least number of perfect square numbers that sum to n.

"""

from math import sqrt


def numSquares(n):
    # We can Use Langrage's 4 Square theorem to do this in very efficient manner
    def is_perfect_square(n):
        square_root = int(sqrt(n))
        return square_root**2 == n

    cpy_n = n
    if is_perfect_square(n):
        return 1
    # 4^k(8m + 7) if in this way a num. can be represented then it's a sum of 4 square nums.
    while n & 3 == 0:  # divisible by 4
        n >>= 2  # divide by 4
    if n & 7 == 7:  # n & 7 ---> n % 8 == 0  and n & 7 == 7 means n % 8 == 7
        return 4
    n = cpy_n
    for i in range(1, int(sqrt(n)) + 1):
        if is_perfect_square(n - i * i):
            return 2
    return 3

    # -----------------------------------------------------

    # # Create a list to store the least number of perfect square numbers that sum to n
    # dp = [0] * (n + 1)

    # for i in range(1, n + 1):
    #     # Initialize the value of dp[i] as the maximum possible value
    #     dp[i] = i
    #     j = 1
    #     while j * j <= i:
    #         # Update the value of dp[i] by taking the minimum of the current value of dp[i] and dp[i - j * j] + 1
    #         dp[i] = min(dp[i], dp[i - j * j] + 1)
    #         j += 1

    # return dp[n]

    # -----------------------------------------------------

    # # 1. Create a list of perfect squares less than or equal to n
    # perfect_squares = [i**2 for i in range(1, int(sqrt(n)) + 1)]
    # print(perfect_squares)

    # # 2. Create a list of length n+1 and initialize it with n+1
    # dp = [n + 1] * (n + 1)
    # dp[0] = 0
    # print(dp)

    # # 3. Iterate through the perfect squares list
    # for square in perfect_squares:
    #     for i in range(square, n + 1):
    #         dp[i] = min(dp[i], dp[i - square] + 1)
    # print(dp)
    # return dp[n]

    # -----------------------------------------------------

    # Create a list of perfect squares
    # squares = [i**2 for i in range(1, int(sqrt(n)) + 1)]
    # print(squares)

    # # Create a list of length n+1 and initialize it with n+1
    # dp = [n + 1] * (n + 1)
    # dp[0] = 0
    # print(dp)

    # for i in range(1, n + 1):
    #     for square in squares:
    #         if i >= square:
    #             dp[i] = min(dp[i], dp[i - square] + 1)
    # print(dp)
    # return dp[n]

    # -----------------------------------------------------

    # my attempt
    #
    # count = 0
    # val = n

    # for i in range(n, 1, -1):
    #     if sqrt(i).is_integer():
    #         print("i", i)
    #         while val > i:
    #             print("val", val)
    #             if val - i >= 0:
    #                 val -= i
    #                 count += 1
    #                 print("val-after", val)
    #                 print("count", count)
    #             else:
    #                 print("else")
    #                 break

    # print(count)
    # return count


# numSquares(12)
# numSquares(50)
# numSquares(100)
