"""
    1508. Range Sum of Sorted Subarray Sums
    https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

    You are given the array nums consisting of n positive integers. You computed the sum of all non-empty
    continuous subarrays from the array and then sorted them in non-decreasing order, creating a new
    array of n * (n + 1) / 2 numbers.

    Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array.
    Since the answer can be a huge number return it modulo 109 + 7.

"""

from typing import List


# all subarrays of [1,2,3,4]
# [[1],[1,2],[1,2,3],[1,2,3,4],[2],[2,3],[2,3,4],[3],[3,4],[4]]


#! --- all me solution !! ---
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        s = []
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                # print(nums[i:j])
                s.append(sum(nums[i:j]))
        # print(sorted(s))
        a = sorted(s)
        ttl = 0
        for i in range(left - 1, right):
            ttl += a[i]
        return ttl % (10**9 + 7)


#! Approach 1: Brute Force
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        store_subarray = []
        for i in range(len(nums)):
            sum = 0
            # Iterate through all indices ahead of the current index.
            for j in range(i, len(nums)):
                sum += nums[j]
                store_subarray.append(sum)

        # Sort all subarray sum values in increasing order.
        store_subarray.sort()

        # Find the sum of all values between left and right.
        range_sum = 0
        mod = 10**9 + 7
        for i in range(left - 1, right):
            range_sum = (range_sum + store_subarray[i]) % mod
        return range_sum


#! Approach 2: Priority Queue
from heapq import heappop, heappush


class Solution:

    def rangeSum(self, nums, n, left, right):
        pq = []
        for i in range(n):
            heappush(pq, (nums[i], i))

        ans = 0
        mod = 1e9 + 7
        for i in range(1, right + 1):
            p = heappop(pq)
            # If the current index is greater than or equal to left, add the
            # value to the answer.
            if i >= left:
                ans = (ans + p[0]) % mod
            # If index is less than the last index, increment it and add its
            # value to the first pair value.
            if p[1] < n - 1:
                p = (p[0] + nums[p[1] + 1], p[1] + 1)
                heappush(pq, p)
        return int(ans)


#! Approach 3: Binary Search and Sliding Window
class Solution:
    def rangeSum(self, nums, n, left, right):
        mod = 10**9 + 7

        def count_and_sum(nums, n, target):
            count = 0
            current_sum = 0
            total_sum = 0
            window_sum = 0
            i = 0
            for j in range(n):
                current_sum += nums[j]
                window_sum += nums[j] * (j - i + 1)
                while current_sum > target:
                    window_sum -= current_sum
                    current_sum -= nums[i]
                    i += 1
                count += j - i + 1
                total_sum += window_sum
            return count, total_sum

        def sum_of_first_k(nums, n, k):
            min_sum = min(nums)
            max_sum = sum(nums)
            left = min_sum
            right = max_sum

            while left <= right:
                mid = left + (right - left) // 2
                if count_and_sum(nums, n, mid)[0] >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            count, total_sum = count_and_sum(nums, n, left)
            # There can be more subarrays with the same sum of left.
            return total_sum - left * (count - k)

        result = (
            sum_of_first_k(nums, n, right) - sum_of_first_k(nums, n, left - 1)
        ) % mod
        # Ensure non-negative result
        return (result + mod) % mod


#! WTF
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MODULI = 10**9 + 7

        # Compute the first- and second-order cumulative sums.
        s1 = [0]
        for i in nums:
            s1.append(s1[-1] + i)

        s2 = [0]
        for i in s1:
            s2.append(s2[-1] + i)

        # Implement the function get_le(x), which returns the number of non-empty subarrays with sums at most x.
        def nvals_le(x: int) -> int:
            if x <= 0:
                return 0

            ret = 0
            lptr = 0
            for rptr in range(1, n + 1):
                while s1[rptr] - s1[lptr] > x:
                    lptr += 1
                ret += rptr - lptr

            return ret

        # Implement the function ind2val(ind), which returns the ind-th smallest non-empty subarray sum.
        def ind2val(ind: int) -> int:
            min_ = 0
            max_ = s1[n]
            while min_ < max_:
                mid = min_ + ((max_ - min_) >> 1)
                if nvals_le(mid) < ind:
                    min_ = mid + 1
                else:
                    max_ = mid

            return min_

        # Calculate ind2val(left) and ind2val(right)
        val_left = ind2val(left)
        val_right = ind2val(right)
        # print(f"val_left = {val_left}, val_right = {val_right}")

        # Case 1: If ind2val(left) == ind2val(right), then the sorted subarray sums are constant between the indices left and right inclusive.  Calculate the result as val_left * (right - left + 1).
        if val_left == val_right:
            return val_left * (right - left + 1) % MODULI

        # Case 2: If ind2val(left) < ind2val(right), calculate the index range (left_exc, right_exc] of the sorted subarray sums that correspond to the values strictly between ind2val(left) and ind2val(right).
        left_exc = nvals_le(val_left)
        right_exc = nvals_le(val_right - 1)
        ret = (
            val_left * (left_exc - (left - 1)) + val_right * (right - right_exc)
        ) % MODULI

        if val_left + 1 <= val_right - 1:
            head_l = head_r = tail = 0

            while s1[tail] < val_left + 1 and tail <= n:
                tail += 1

            while tail <= n:
                # find the least head_l such that sum(nums[head_l:tail]) <= val_right - 1
                while s1[tail] - s1[head_l] > val_right - 1:
                    head_l += 1

                # find the greatest head_r such that sum(nums[head_r:tail]) >= val_left + 1
                while s1[tail] - s1[head_r + 1] >= val_left + 1:
                    head_r += 1

                if head_l <= head_r:
                    ret = (
                        ret
                        + s1[tail] * (head_r - head_l + 1)
                        - (s2[head_r + 1] - s2[head_l])
                    ) % MODULI
                    # print(f"head: {head_l} to {head_r}, tail: {tail}, total: {ret}")

                tail += 1
            # print()

        return ret
