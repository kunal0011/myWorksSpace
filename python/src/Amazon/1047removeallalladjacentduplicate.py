class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            # If the stack is not empty and the top of the stack is equal to the current char
            if stack and stack[-1] == char:
                stack.pop()  # Remove the duplicate
            else:
                stack.append(char)  # Push the current character onto the stack

        # Join the characters in the stack to form the result string
        return ''.join(stack)

# Testing the implementation


def test_remove_duplicates():
    solution = Solution()

    # Test case 1
    s1 = "abbaca"
    # Expected output: "ca" (remove "bb" -> "aaca", then remove "aa" -> "ca")
    result1 = solution.removeDuplicates(s1)
    print(f"Test 1 - Result: {result1}, Expected: ca")

    # Test case 2
    s2 = "azxxzy"
    # Expected output: "ay" (remove "xx" -> "azzy", then remove "zz" -> "ay")
    result2 = solution.removeDuplicates(s2)
    print(f"Test 2 - Result: {result2}, Expected: ay")

    # Test case 3
    s3 = "aabbccddeeff"
    # Expected output: "" (All adjacent characters are removed)
    result3 = solution.removeDuplicates(s3)
    print(f"Test 3 - Result: {result3}, Expected: ")


# Run the test
test_remove_duplicates()
