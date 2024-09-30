class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        j = 0  # Pointer for popped array

        # Simulate the push and pop operations
        for x in pushed:
            stack.append(x)  # Push the current element onto the stack
            # Check if the top of the stack matches the current popped element
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        # If the stack is empty, all elements have been successfully popped
        return len(stack) == 0

# Testing the implementation


def test_validate_stack_sequences():
    solution = Solution()

    # Test case 1
    pushed1 = [1, 2, 3, 4, 5]
    popped1 = [4, 5, 3, 2, 1]
    # Expected output: True (Valid sequence)
    result1 = solution.validateStackSequences(pushed1, popped1)
    print(f"Test 1 - Result: {result1}, Expected: True")

    # Test case 2
    pushed2 = [1, 2, 3, 4, 5]
    popped2 = [4, 3, 5, 1, 2]
    # Expected output: False (Invalid sequence)
    result2 = solution.validateStackSequences(pushed2, popped2)
    print(f"Test 2 - Result: {result2}, Expected: False")

    # Test case 3
    pushed3 = [2, 1, 0]
    popped3 = [1, 2, 0]
    # Expected output: True (Valid sequence)
    result3 = solution.validateStackSequences(pushed3, popped3)
    print(f"Test 3 - Result: {result3}, Expected: True")


# Run the test
test_validate_stack_sequences()
