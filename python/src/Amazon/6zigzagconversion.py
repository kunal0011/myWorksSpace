# ### Problem Statement
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

# ```
# P   A   H   N
# A P L S I I G
# Y   I   R
# ```

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows.

# ### Example 1:
# ```
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# ```

# ### Example 2:
# ```
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# ```

# ### Example 3:
# ```
# Input: s = "A", numRows = 1
# Output: "A"
# ```

# ### Solution Logic
# 1. If `numRows` is 1, return the string as is because the zigzag pattern is not applicable.
# 2. Create an array of strings to represent each row.
# 3. Iterate through the characters of the string, appending each character to the appropriate row.
# 4. Use a variable to track the current row and a direction flag to determine whether to move up or down the rows.
# 5. After processing all characters, concatenate the rows to form the final result.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings for each row
        rows = [''] * numRows
        cur_row = 0  # Start from the first row
        going_down = False  # Direction of traversal

        # Traverse through the string
        for c in s:
            rows[cur_row] += c  # Place the character in the current row
            # If we are at the first or last row, reverse the direction
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            # Move to the next row, either up or down
            cur_row += 1 if going_down else -1

        # Join all rows to form the final string
        return ''.join(rows)

# Test the Solution class


def test_solution():
    sol = Solution()

    # Test case 1
    assert sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

    # Test case 2
    assert sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

    # Test case 3
    assert sol.convert("AB", 1) == "AB"

    print("All test cases passed!")


# Run the tests
test_solution()
