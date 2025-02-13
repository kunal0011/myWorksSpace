"""
LeetCode 118. Pascal's Triangle

Problem Statement:
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Pascal's Triangle visualization:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Constraints:
- 1 <= numRows <= 30
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generate Pascal's Triangle using dynamic programming.
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        # Initialize triangle with first row
        triangle = [[1]]

        # Generate subsequent rows
        for i in range(1, numRows):
            # Previous row
            prev_row = triangle[-1]
            # Current row always starts with 1
            current_row = [1]

            # Calculate middle elements
            for j in range(1, i):
                current_row.append(prev_row[j-1] + prev_row[j])

            # Current row always ends with 1
            current_row.append(1)
            triangle.append(current_row)

        return triangle

    def generateMathematical(self, numRows: int) -> List[List[int]]:
        """
        Generate Pascal's Triangle using mathematical combinations.
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        def combination(n: int, k: int) -> int:
            """Calculate C(n,k) efficiently"""
            if k > n - k:  # Optimize by using smaller k
                k = n - k

            result = 1
            for i in range(k):
                result *= (n - i)
                result //= (i + 1)
            return result

        triangle = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                row.append(combination(i, j))
            triangle.append(row)

        return triangle


def print_triangle(triangle: List[List[int]], centered: bool = True) -> None:
    """
    Helper function to print Pascal's Triangle in a visually appealing format.
    """
    if not triangle:
        return

    # Calculate the width needed for the largest number
    max_num_width = len(str(max(max(row) for row in triangle)))
    # Calculate the width needed for the bottom row
    max_width = len(str.join(" ", (str(x).center(max_num_width)
                    for x in triangle[-1])))

    for row in triangle:
        # Convert numbers to strings with consistent width
        numbers = [str(x).center(max_num_width) for x in row]
        # Join numbers with spaces
        line = str.join(" ", numbers)
        # Center the entire line if requested
        if centered:
            line = line.center(max_width)
        print(line)


def test_pascal_triangle():
    solution = Solution()

    test_cases = [
        {
            "numRows": 5,
            "description": "Standard case"
        },
        {
            "numRows": 1,
            "description": "Single row"
        },
        {
            "numRows": 2,
            "description": "Two rows"
        },
        {
            "numRows": 7,
            "description": "Larger triangle"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        numRows = test_case["numRows"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Number of rows: {numRows}")

        # Test both implementations
        result_dp = solution.generate(numRows)
        result_math = solution.generateMathematical(numRows)

        print("\nDynamic Programming approach result:")
        print_triangle(result_dp)

        print("\nMathematical approach result:")
        print_triangle(result_math)

        # Verify both implementations give same result
        assert result_dp == result_math, \
            f"Implementations gave different results:\nDP: {result_dp}\nMath: {result_math}"

        # Verify properties of Pascal's Triangle
        for row_idx, row in enumerate(result_dp):
            # Verify row length
            assert len(row) == row_idx + 1, \
                f"Row {row_idx} has incorrect length: {len(row)}"

            # Verify symmetry
            assert row == row[::-1], \
                f"Row {row_idx} is not symmetric: {row}"

            # Verify first and last elements are 1
            assert row[0] == row[-1] == 1, \
                f"Row {row_idx} does not start and end with 1: {row}"

        print("✓ Test case passed!")


if __name__ == "__main__":
    test_pascal_triangle()
    print("\nAll test cases passed! 🎉")
