"""
LeetCode 225 - Implement Stack using Queues

Problem Statement:
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support
all the functions of a normal stack (push, top, pop, and empty).

Solution Logic:
1. Use two queues: q1 (primary) and q2 (auxiliary)
2. Push: Always add to q1 O(1)
3. Pop/Top: 
   - Move n-1 elements from q1 to q2
   - Last element in q1 is stack top
   - For pop: remove it, for top: move it to q2
   - Swap q1 and q2
4. Time: Push O(1), Pop/Top O(n), Empty O(1)
5. Space: O(n)
"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()  # Primary queue for push
        self.q2 = deque()  # Temporary queue for pop

    def push(self, x: int) -> None:
        # Push element to q1
        self.q1.append(x)

    def pop(self) -> int:
        # Move elements from q1 to q2 until only one element is left in q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # The last remaining element is the "top" of the stack
        result = self.q1.popleft()

        # Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        # Move elements from q1 to q2 until only one element is left in q1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        # The last element is the "top" of the stack
        result = self.q1.popleft()
        self.q2.append(result)  # Put the last element into q2

        # Swap the names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        return result

    def empty(self) -> bool:
        # If q1 is empty, the stack is empty
        return not self.q1

def test_stack_using_queues():
    # Test Case 1: Basic operations
    print("Test 1: Basic Operations")
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(f"Top element: {stack.top()}")    # Expected: 2
    print(f"Pop element: {stack.pop()}")    # Expected: 2
    print(f"Is empty? {stack.empty()}")     # Expected: False
    
    # Test Case 2: Multiple pops
    print("\nTest 2: Multiple Operations")
    stack2 = MyStack()
    stack2.push(1)
    stack2.push(2)
    stack2.push(3)
    print(f"Pop three times: {stack2.pop()}, {stack2.pop()}, {stack2.pop()}")
    print(f"Is empty? {stack2.empty()}")    # Expected: True
    
    # Test Case 3: Push after pop
    print("\nTest 3: Push after Pop")
    stack3 = MyStack()
    stack3.push(1)
    stack3.pop()
    stack3.push(2)
    print(f"Top element: {stack3.top()}")   # Expected: 2

if __name__ == "__main__":
    test_stack_using_queues()
