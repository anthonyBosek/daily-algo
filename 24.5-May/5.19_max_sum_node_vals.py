"""
    3068. Find the Maximum Sum of Node Values
    https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

    There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

    Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

        • Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
            · nums[u] = nums[u] XOR k
            · nums[v] = nums[v] XOR k

    Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.

"""

# from math import inf


def maximumValueSum(nums, k, edges):
    """
    :type nums: List[int]
    :type k: int
    :type edges: List[List[int]]
    :rtype: int
    """
    # best_sum = sum(max(n, k ^ n) for n in nums)
    # cnt = sum((n ^ k) > n for n in nums)
    # return best_sum - (min(abs(n - (n ^ k)) for n in nums) if cnt % 2 else 0)

    # ? ----------------------------------------------------------------------------

    # n, res, minD, cnt = len(nums), 0, inf, 0
    # for num in nums:
    #     d = (num ^ k) - num
    #     if d > 0:
    #         cnt ^= 1
    #         if d < minD:
    #             minD = d
    #         res += num ^ k
    #     else:
    #         if -d < minD:
    #             minD = -d
    #         res += num
    # if cnt:
    #     res -= minD
    # return res

    # ? ----------------------------------------------------------------------------

    n: int = len(nums)
    ## temp[current_index(node)][is_even]
    temp: list[list[int]] = [[-1 for _ in range(2)] for _ in range(n)]

    ## cur_ind -> cur_index of the tree and is_even represents whether we have already changed (XOR) even or odd number of nodes
    def calculate_max(cur_ind, is_even) -> int:
        ## if we go to node which doesn't exist
        if cur_ind == n:
            return 0 if is_even else -float("inf")
        ## if we've already encountered this state
        if temp[cur_ind][is_even] != -1:
            return temp[cur_ind][is_even]

        ## checking all possible variants (no XOR or XOR)
        ## we don't change the number of XOR nodes
        no_xor = nums[cur_ind] + calculate_max(cur_ind + 1, is_even)
        ## we added 1 XORed node
        with_xor = (nums[cur_ind] ^ k) + calculate_max(cur_ind + 1, not is_even)

        mx_possible = max(no_xor, with_xor)
        temp[cur_ind][is_even] = mx_possible
        return mx_possible

    ## is_even == 1 because we have XORed 0 nodes which is even
    return calculate_max(0, 1)
