# LeetCode 7: "Reverse Integer"

# Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return 0.

# ### Example 1:
# ```
# Input: x = 123
# Output: 321
# ```

# ### Example 2:
# ```
# Input: x = -123
# Output: -321
# ```

# ### Example 3:
# ```
# Input: x = 120
# Output: 21
# ```

# ### Example 4:
# ```
# Input: x = 0
# Output: 0
# ```

# ### Constraints:
# - `-2^31 <= x <= 2^31 - 1`

# ### Solution Logic
# 1. Handle the sign of the integer.
# 2. Reverse the digits of the absolute value of the integer.
# 3. Check if the reversed integer overflows the 32-bit signed integer range.
# 4. Return the reversed integer with the original sign if it does not overflow, otherwise return 0.

class Solution:
    def reverse(self, x: int) -> int:

        x = list(str(x)[::-1])
        if x[-1] == '-':
            x.remove('-')
            x.insert(0, '-')
        x = ''.join(x)
        max_val = pow(2, 31)-1
        min_val = -pow(2, 31)
        x = int(x)
        if x <= max_val and x >= min_val:
            return x
        else:
            return 0


def test_reverse():
    solution = Solution()

    # Test case 1: Positive number
    x = 123
    expected = 321
    result = solution.reverse(x)
    print(
        f"Test case 1 - Input: {x}, Expected: {expected}, Result: {result}, Passed: {result == expected}")

    # Test case 2: Negative number
    x = -123
    expected = -321
    result = solution.reverse(x)
    print(
        f"Test case 2 - Input: {x}, Expected: {expected}, Result: {result}, Passed: {result == expected}")

    # Test case 3: Number with trailing zero
    x = 120
    expected = 21
    result = solution.reverse(x)
    print(
        f"Test case 3 - Input: {x}, Expected: {expected}, Result: {result}, Passed: {result == expected}")

    # Test case 4: Zero
    x = 0
    expected = 0
    result = solution.reverse(x)
    print(
        f"Test case 4 - Input: {x}, Expected: {expected}, Result: {result}, Passed: {result == expected}")

    # Test case 5: Overflow positive
    x = 1534236469
    expected = 0
    result = solution.reverse(x)
    print(
        f"Test case 5 - Input: {x}, Expected: {expected}, Result: {result}, Passed: {result == expected}")

    # Test case 6: Overflow negative
    x = -1534236469
    expected = 0
    result = solution.reverse(x)
    print(
        f"Test case 6 - Input: {x}, Expected: {expected}, Result: {result}, Passed: {result == expected}")


# Run the test cases
test_reverse()
