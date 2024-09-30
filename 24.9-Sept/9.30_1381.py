"""
    1381. Design a Stack With Increment Operation
    https://leetcode.com/problems/design-a-stack-with-increment-operation/

    Design a stack that supports increment operations on its elements.

    Implement the CustomStack class:

        • CustomStack(int maxSize) Initializes the object with maxSize which is
            the maximum number of elements in the stack.

        • void push(int x) Adds x to the top of the stack if the stack has not
            reached the maxSize.

        • int pop() Pops and returns the top of the stack or -1 if the stack is empty.

        • void inc(int k, int val) Increments the bottom k elements of the stack by val.
            If there are less than k elements in the stack, increment all the elements
            in the stack.

"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


#! Approach 1: Array
class CustomStack:
    def __init__(self, max_size: int):
        # Array to store stack elements
        self._stack = []
        # Index of the top element in the stack
        self._max_size = max_size

    def push(self, x: int) -> None:
        if len(self._stack) < self._max_size:
            self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop() if self._stack else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self._stack))):
            self._stack[i] += val


#! Approach 2: Linked List
from collections import deque


class CustomStack:
    def __init__(self, maxSize: int):
        # Initialize the stack as a deque for efficient add/remove operations
        self.stack = deque()
        self.max_size = maxSize

    def push(self, x: int) -> None:
        # Add the element to the top of the stack if it hasn't reached max_size
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self) -> int:
        # Return -1 if the stack is empty, otherwise remove and return the top element
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        # Increment the bottom k elements (or all elements if k > stack size)
        for i, _ in zip(range(k), self.stack):
            self.stack[i] += val


#! Approach 3: Array using Lazy Propagation
class CustomStack:
    def __init__(self, max_size: int):
        # List to store stack elements
        self._stack = [0] * max_size
        # List to store increments for lazy propagation
        self._inc = [0] * max_size
        # Current top index of the stack
        self._top = -1

    def push(self, x: int) -> None:
        if self._top < len(self._stack) - 1:
            self._top += 1
            self._stack[self._top] = x

    def pop(self) -> int:
        if self._top < 0:
            return -1

        # Calculate the actual value with increment
        result = self._stack[self._top] + self._inc[self._top]

        # Propagate the increment to the element below
        if self._top > 0:
            self._inc[self._top - 1] += self._inc[self._top]

        # Reset the increment for this position
        self._inc[self._top] = 0
        self._top -= 1
        return result

    def increment(self, k: int, val: int) -> None:
        if self._top >= 0:
            # Apply increment to the topmost element of the range
            index = min(self._top, k - 1)
            self._inc[index] += val
