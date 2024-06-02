"""
    344. Reverse String
    https://leetcode.com/problems/reverse-string/

    Write a function that reverses a string. The input string is given as an array of characters s.

    You must do this by modifying the input array in-place with O(1) extra memory.

"""


def reverseString(s):
    """
    s: List[str]
    rtype: None
    Do not return anything, modify s in-place instead.
    """

    #! Solution 1
    # s.reverse()

    #! Solution 2 (mine)
    ## The [::-1] slice is a common Python idiom for creating a reversed copy of a list.
    ## The s[:] on the left side of the assignment replaces the entire contents of the list s with the reversed copy.
    ## The [:] is necessary to modify the original list rather than reassigning s to a new list.
    # s[:] = s[::-1]

    #! Solution 3
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
