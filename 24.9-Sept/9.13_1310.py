"""
    1310. XOR Queries of a Subarray
    https://leetcode.com/problems/xor-queries-of-a-subarray/

    You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

    For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

    Return an array answer where answer[i] is the answer to the ith query.

"""


class Solution:
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(arr)
        prefix_xor = [0] * (n + 1)

        # Calculate prefix XOR
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        # Process each query
        result = []
        for left, right in queries:
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])

        return result

        # px=[0]*(len(arr)+1)
        # a=[]
        # for i in range(len(arr)):
        #     px[i+1]=px[i]^arr[i]
        # for j in queries:
        #     a.append(px[j[1]+1]^px[j[0]])
        # return a


#! Approach 1: Iterative Approach **Timed Out**
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        # Process each query
        for q in queries:
            xor_sum = 0
            # Calculate XOR for the range [q[0], q[1]]
            for i in range(q[0], q[1] + 1):
                xor_sum ^= arr[i]
            result.append(xor_sum)
        return result


#! Approach 2: Prefix XOR Array
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Build prefix XOR array
        prefix_xor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        # Store the XOR result for each query in a variable
        result = [prefix_xor[r + 1] ^ prefix_xor[l] for l, r in queries]
        return result


#! Approach 3: In place Prefix XOR
class Solution:
    def xorQueries(self, arr, queries):
        result = []

        # Step 1: Convert arr into an in-place prefix XOR array
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        # Step 2: Resolve each query using the prefix XOR array
        for left, right in queries:
            if left > 0:
                result.append(arr[left - 1] ^ arr[right])
            else:
                result.append(arr[right])

        return result
