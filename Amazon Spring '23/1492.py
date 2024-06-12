"""
    1492. The kth Factor of n
    https://leetcode.com/problems/the-kth-factor-of-n/

    You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

    Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

"""


def kthFactor(n: int, k: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            if count == k:
                return i
    return -1


# -----------------------------------
# --- Optimized Solution ---
# #? Iterate over the range of 1 to n
# for i in range(1, n + 1):
#     #? If n is divisible by i
#     if n % i == 0:
#         #? Decrement k
#         k -= 1
#         #? If k is zero
#         if k == 0:
#             #? Return i
#             return i
# #? Return -1
# return -1

# -----------------------------------
# --- My Solution ---
# #? Initialize the factors list
# factors = []
# #? Iterate over the range of 1 to n
# for i in range(1, n + 1):
#     #? If n is divisible by i
#     if n % i == 0:
#         #? Append the factor to the list
#         factors.append(i)
# #? If k is greater than the length of the factors list
# if k > len(factors):
#     #? Return -1
#     return -1
# #? Return the kth factor
# return factors[k - 1]
