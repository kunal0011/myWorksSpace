"""
LeetCode 716: Max Stack

Design a max stack data structure that supports the following operations:
- push(x): Pushes element x onto the stack.
- pop(): Removes the element on top of the stack and returns it.
- top(): Gets the element on the top of the stack.
- peekMax(): Retrieves the maximum element in the stack.
- popMax(): Retrieves the maximum element in the stack and removes it.

All operations should run in O(1) average time complexity.
"""

class MaxStack:

    def __init__(self):
        # Stack to store the values
        self.stack = []
        # Stack to store the maximum values at each stage
        self.max_stack = []

    def push(self, x: int) -> None:
        # Push x to the main stack
        self.stack.append(x)
        # Push the max of x and the current max to the max stack
        if self.max_stack:
            self.max_stack.append(max(x, self.max_stack[-1]))
        else:
            self.max_stack.append(x)

    def pop(self) -> int:
        # Pop from both stacks
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        # Return the top of the stack
        return self.stack[-1]

    def peekMax(self) -> int:
        # The top of the max_stack is the current maximum
        return self.max_stack[-1]

    def popMax(self) -> int:
        max_val = self.peekMax()
        temp_stack = []
        
        # Remove elements until we find max_val
        while self.stack and self.top() != max_val:
            temp_stack.append(self.pop())
        
        # Remove the max value
        self.pop()
        
        # Restore the elements in original order
        while temp_stack:
            self.push(temp_stack.pop())
            
        return max_val

# Test driver
def test_max_stack():
    # Test case 1: Basic operations
    print("Test Case 1: Basic operations")
    stack = MaxStack()
    operations = ["push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
    values = [5, 1, 5, None, None, None, None, None, None]
    expected = [None, None, None, 5, 5, 1, 5, 1, 5]
    
    for i, (op, val) in enumerate(zip(operations, values)):
        result = None
        if op == "push":
            result = stack.push(val)
        elif op == "pop":
            result = stack.pop()
        elif op == "top":
            result = stack.top()
        elif op == "peekMax":
            result = stack.peekMax()
        elif op == "popMax":
            result = stack.popMax()
        
        print(f"Operation: {op}, Value: {val}, Result: {result}, Expected: {expected[i]}")
        assert result == expected[i], f"Test failed! Expected {expected[i]} but got {result}"
    
    # Test case 2: Multiple popMax operations
    print("\nTest Case 2: Multiple popMax operations")
    stack = MaxStack()
    for x in [3, 2, 5, 4, 1]:
        stack.push(x)
    
    assert stack.popMax() == 5, "Expected max value 5"
    assert stack.popMax() == 4, "Expected max value 4"
    assert stack.top() == 1, "Expected top value 1"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_max_stack()
