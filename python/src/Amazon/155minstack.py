"""
LeetCode 155. Min Stack

Problem Statement:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
- -2^31 <= val <= 2^31 - 1
- Methods pop, top and getMin operations will always be called on non-empty stacks
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin
"""


class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        Using two stacks: one for values and one for minimum values.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Push element val onto stack.
        Also push to min_stack if val is less than or equal to current minimum.
        """
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        Also pop from min_stack if the popped value was the minimum.
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None


def test_min_stack():
    """Test function with various test cases."""
    # Test case 1: Basic operations
    print("Test case 1: Basic operations")
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3, "getMin should return -3"
    min_stack.pop()
    assert min_stack.top() == 0, "top should return 0"
    assert min_stack.getMin() == -2, "getMin should return -2"
    print("✓ Basic operations test passed")

    # Test case 2: Multiple minimum values
    print("\nTest case 2: Multiple minimum values")
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(1)
    assert min_stack.getMin() == 1, "getMin should return 1"
    min_stack.pop()
    assert min_stack.getMin() == 1, "getMin should still return 1"
    print("✓ Multiple minimum values test passed")

    # Test case 3: Ascending order
    print("\nTest case 3: Ascending order")
    min_stack = MinStack()
    min_stack.push(1)
    min_stack.push(2)
    min_stack.push(3)
    assert min_stack.getMin() == 1, "getMin should return 1"
    min_stack.pop()
    assert min_stack.getMin() == 1, "getMin should still return 1"
    print("✓ Ascending order test passed")

    # Test case 4: Descending order
    print("\nTest case 4: Descending order")
    min_stack = MinStack()
    min_stack.push(3)
    min_stack.push(2)
    min_stack.push(1)
    assert min_stack.getMin() == 1, "getMin should return 1"
    min_stack.pop()
    assert min_stack.getMin() == 2, "getMin should return 2"
    print("✓ Descending order test passed")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_min_stack()
