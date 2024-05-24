"""
    232. Implement Queue using Stacks
    https://leetcode.com/problems/implement-queue-using-stacks/

    Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

"""

from collections import deque


class MyQueue:
    def __init__(self):
        # self.my_que = []
        self.my_que = deque([])

    def push(self, x: int) -> None:
        self.my_que.append(x)

    def pop(self) -> int:
        # return self.my_que.pop(0)
        return self.my_que.popleft()

    def peek(self) -> int:
        return self.my_que[0]

    def empty(self) -> bool:
        return len(self.my_que) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
