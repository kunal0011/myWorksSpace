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
