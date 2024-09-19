"""
    241. Different Ways to Add Parentheses
    https://leetcode.com/problems/different-ways-to-add-parentheses/

    Given a string expression of numbers and operators, return all possible results from computing all
    the different possible ways to group numbers and operators. You may return the answer in any order.

    The test cases are generated such that the output values fit in a 32-bit integer and the number of
    different results does not exceed 104.

"""


def diffWaysToCompute(expression):
    """
    :type expression: str
    :rtype: List[int]
    """
    pass


#! Approach 1: Recursion
class Solution:
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        results = []

        # Base case: if the string is empty, return an empty list
        if len(expression) == 0:
            return results

        # Base case: if the string is a single character, treat it as a number and return it
        if len(expression) == 1:
            return [int(expression)]

        # If the string has only two characters and the first character is a digit, parse it as a number
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]

        # Recursive case: iterate through each character
        for i, current_char in enumerate(expression):

            # Skip if the current character is a digit
            if current_char.isdigit():
                continue

            # Split the expression into left and right parts
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i + 1 :])

            # Combine results from left and right parts
            for left_value in left_results:
                for right_value in right_results:
                    # Perform the operation based on the current character
                    if current_char == "+":
                        results.append(left_value + right_value)
                    elif current_char == "-":
                        results.append(left_value - right_value)
                    elif current_char == "*":
                        results.append(left_value * right_value)

        return results


#! Approach 2: Memoization
class Solution:
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # Initialize memoization dictionary to store results of subproblems
        memo = {}
        # Solve for the entire expression
        return self._compute_results(expression, memo, 0, len(expression) - 1)

    def _compute_results(self, expression, memo, start, end):
        """
        :type expression: str
        :type memo: dict
        :type start: int
        :type end: int
        :rtype: List[int]
        """
        # If result is already memoized, return it
        if (start, end) in memo:
            return memo[(start, end)]

        results = []

        # Base case: single digit
        if start == end:
            results.append(int(expression[start]))
            return results

        # Base case: two-digit number
        if end - start == 1 and expression[start].isdigit():
            results.append(int(expression[start : end + 1]))
            return results

        # Recursive case: split the expression at each operator
        for i in range(start, end + 1):
            if expression[i].isdigit():
                continue

            left_results = self._compute_results(expression, memo, start, i - 1)
            right_results = self._compute_results(expression, memo, i + 1, end)

            # Combine results from left and right subexpressions
            for left_value in left_results:
                for right_value in right_results:
                    if expression[i] == "+":
                        results.append(left_value + right_value)
                    elif expression[i] == "-":
                        results.append(left_value - right_value)
                    elif expression[i] == "*":
                        results.append(left_value * right_value)

        # Memoize the result for this subproblem
        memo[(start, end)] = results

        return results


#! Approach 3: Tabulation
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        # Create a 2D array of lists to store results of subproblems
        dp = [[[] for _ in range(n)] for _ in range(n)]

        self._initialize_base_cases(expression, dp)

        # Fill the dp table for all possible subexpressions
        for length in range(3, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                self._process_subexpression(expression, dp, start, end)

        # Return the results for the entire expression
        return dp[0][n - 1]

    def _initialize_base_cases(self, expression: str, dp: List[List[List[int]]]):
        # Handle base cases: single digits and two-digit numbers
        for i, char in enumerate(expression):
            if char.isdigit():
                # Check if it's a two-digit number
                dig1 = ord(char) - ord("0")
                if i + 1 < len(expression) and expression[i + 1].isdigit():
                    dig2 = ord(expression[i + 1]) - ord("0")
                    number = dig1 * 10 + dig2
                    dp[i][i + 1].append(number)
                # Single digit case
                dp[i][i].append(dig1)

    def _process_subexpression(
        self, expression: str, dp: List[List[List[int]]], start: int, end: int
    ):
        # Try all possible positions to split the expression
        for split in range(start, end + 1):
            if expression[split].isdigit():
                continue

            left_results = dp[start][split - 1]
            right_results = dp[split + 1][end]

            self._compute_results(
                expression[split], left_results, right_results, dp[start][end]
            )

    def _compute_results(
        self,
        op: str,
        left_results: List[int],
        right_results: List[int],
        results: List[int],
    ):
        # Compute results based on the operator at position 'split'
        for left_value in left_results:
            for right_value in right_results:
                if op == "+":
                    results.append(left_value + right_value)
                elif op == "-":
                    results.append(left_value - right_value)
                elif op == "*":
                    results.append(left_value * right_value)
