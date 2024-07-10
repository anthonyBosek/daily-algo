"""
    1598. Crawler Log Folder
    https://leetcode.com/problems/crawler-log-folder/

    The Leetcode file system keeps a log each time some user performs a change folder operation.

    The operations are described below:

        • "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
        • "./" : Remain in the same folder.
        • "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

    You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

    The file system starts in the main folder, then the operations in logs are performed.

    Return the minimum number of operations needed to go back to the main folder after the change folder operations.

"""


def minOperations(logs):
    """
    :type logs: List[str]
    :rtype: int
    """
    stack = []
    for log in logs:
        if log == "../":
            if stack:
                stack.pop()
        elif log == "./":
            continue
        else:
            stack.append(log)
    return len(stack)


# ----------------------------------------------------------

from typing import List


#! Approach 1: Counter
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_depth = 0

        # Iterate through each log operation
        for current_operation in logs:
            # Go up one directory if "../" is encountered, but don't go above the root
            if current_operation == "../":
                folder_depth = max(0, folder_depth - 1)
            # Increase depth if the log is not 'stay in the current directory'
            elif current_operation != "./":
                # Go down one directory
                folder_depth += 1
            # Ignore "./" operations as they don't change the current folder

        return folder_depth


#! Approach 2: Stack
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_stack = []

        for current_operation in logs:
            if current_operation == "../":
                # Move up to parent directory if not already at main folder
                if folder_stack:
                    folder_stack.pop()
            elif current_operation != "./":
                # Enter a new folder
                folder_stack.append(current_operation)
            # Ignore "./" operations as they don't change the current folder
        # The stack size represents the number of folders deep we are
        return len(folder_stack)
