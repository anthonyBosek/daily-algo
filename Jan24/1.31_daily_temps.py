"""
    739. Daily Temperatures
    https://leetcode.com/problems/daily-temperatures/

    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
        is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day
        for which this is possible, keep answer[i] == 0 instead.

"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        This is a simple stack problem. We will use stack to store the index of the temperatures. We will iterate
            through the temperatures and while the stack is not empty and the current temperature is greater than the
            temperature at the top of the stack, we will pop the index from the stack and calculate the difference
            between the current index and the popped index and store it in the result array at the popped index. Then we
            will continue this process until the stack is empty or the current temperature is not greater than the
            temperature at the top of the stack. Then we will push the current index to the stack.

        :param temperatures: list of integers
        :return: list of integers
        """
        # stack = []
        # result = [0] * len(temperatures)
        # for i, t in enumerate(temperatures):
        #     while stack and t > temperatures[stack[-1]]:
        #         j = stack.pop()
        #         result[j] = i - j
        #     stack.append(i)
        # return result

        # ------------------------------------------------------------------------------------------------------------------

        """
        The idea is to use a stack to keep track of the indices of the temperatures. We will iterate through the
            temperatures and for each temperature, we will check if the current temperature is greater than the
            temperature at the top of the stack. If it is, we will pop the top of the stack and calculate the difference
            between the current index and the index at the top of the stack. We will keep doing this until the stack is
            empty or the current temperature is less than the temperature at the top of the stack. Then we will push the
            current index onto the stack. This way, we will keep track of the indices of the temperatures that we are
            waiting for a warmer temperature.
        """

        # stack = []
        # answer = [0] * len(temperatures)

        # for i, temp in enumerate(temperatures):
        #     while stack and temp > temperatures[stack[-1]]:
        #         j = stack.pop()
        #         answer[j] = i - j
        #     stack.append(i)

        # return answer

        # ------------------------------------------------------------------------------------------------------------------

        """
        :param temperatures: list of integers
        :return: list of integers
        """
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                result[j] = i - j
            stack.append(i)
        return result
