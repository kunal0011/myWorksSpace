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
        # Get the maximum value
        max_val = self.peekMax()
        # Temp stack to hold elements until we find the max
        buffer = []
        # Remove elements from the stack until we find the max
        while self.top() != max_val:
            buffer.append(self.pop())
        # Pop the maximum element
        self.pop()
        # Restore the removed elements
        while buffer:
            self.push(buffer.pop())
        return max_val
