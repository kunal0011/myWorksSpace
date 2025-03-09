"""
LeetCode 232 - Implement Queue using Stacks

Problem Statement:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should 
support all the functions of a normal queue (push, peek, pop, and empty).

Solution Logic:
1. Use two stacks: stack1 (for push) and stack2 (for pop/peek)
2. Push: Always add to stack1 O(1)
3. Pop/Peek: 
   - If stack2 is empty, move all elements from stack1 to stack2
   - This reverses their order, making oldest element on top
   - Return top of stack2
4. Time: Push O(1), Pop amortized O(1), Peek O(1)
5. Space: O(n)
"""

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self._move_elements()
        return self.stack2.pop()

    def peek(self) -> int:
        self._move_elements()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    def _move_elements(self) -> None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

def test_queue():
    # Test Case 1: Basic operations
    print("Test 1: Basic Operations")
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(f"First element: {queue.peek()}")    # Expected: 1
    print(f"Pop element: {queue.pop()}")       # Expected: 1
    print(f"Is empty? {queue.empty()}")        # Expected: False
    
    # Test Case 2: Multiple operations
    print("\nTest 2: Multiple Operations")
    queue2 = MyQueue()
    queue2.push(1)
    queue2.push(2)
    queue2.push(3)
    print(f"Pop first: {queue2.pop()}")        # Expected: 1
    queue2.push(4)
    print(f"Pop sequence: {queue2.pop()}, {queue2.pop()}, {queue2.pop()}")  # Expected: 2,3,4
    
    # Test Case 3: Empty queue operations
    print("\nTest 3: Empty Queue")
    queue3 = MyQueue()
    print(f"Is empty? {queue3.empty()}")       # Expected: True
    queue3.push(1)
    queue3.pop()
    print(f"Is empty after pop? {queue3.empty()}")  # Expected: True

if __name__ == "__main__":
    test_queue()
