"""
LeetCode 120. Triangle

Problem Statement:
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, 
if you are on index i on the current row, you may move to either index i or index i + 1 
on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is: 2 + 3 + 5 + 1 = 11

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -10^4 <= triangle[i][j] <= 10^4
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Bottom-up Dynamic Programming with O(n) space.
        Time complexity: O(n^2) where n is the number of rows
        Space complexity: O(n)
        """
        # Start with the bottom row
        min_path = triangle[-1][:]

        # Work our way up
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # For each position, choose the minimum of the two possible paths below
                min_path[col] = triangle[row][col] + \
                    min(min_path[col], min_path[col + 1])

        return min_path[0]

    def minimumTotalTopDown(self, triangle: List[List[int]]) -> int:
        """
        Top-down Dynamic Programming with memoization.
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        memo = {}

        def dfs(row: int, col: int) -> int:
            # Base cases
            if row == len(triangle):
                return 0
            if (row, col) in memo:
                return memo[(row, col)]

            # Calculate minimum path sum from current position
            current = triangle[row][col]
            if row < len(triangle) - 1:
                current += min(dfs(row + 1, col),      # Move to same column
                               dfs(row + 1, col + 1))    # Move to next column

            memo[(row, col)] = current
            return current

        return dfs(0, 0)

    def minimumTotal2D(self, triangle: List[List[int]]) -> int:
        """
        2D Dynamic Programming solution for better visualization.
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        n = len(triangle)
        # Initialize dp array with max values
        dp = [[float('inf')] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        # Fill the dp array
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:  # Leftmost element
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:  # Rightmost element
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:  # Middle elements
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        # Return minimum value in the bottom row
        return min(dp[-1])


def print_triangle_with_path(triangle: List[List[int]], path: List[int] = None) -> None:
    """Helper function to visualize triangle and minimum path"""
    max_width = len(' '.join(map(str, triangle[-1])))

    for i, row in enumerate(triangle):
        # Convert row to strings and pad with spaces
        row_str = [str(num).rjust(3) for num in row]

        # Highlight path if provided
        if path and i < len(path):
            row_str[path[i]] = f"[{str(triangle[i][path[i]]).rjust(1)}]"

        # Center the row
        print(' '.join(row_str).center(max_width))


def find_min_path(triangle: List[List[int]], min_sum: int) -> List[int]:
    """Helper function to reconstruct minimum path"""
    path = []
    current_sum = min_sum
    current_pos = 0

    for i in range(len(triangle)):
        # Find the position in current row that leads to minimum sum
        if i == len(triangle) - 1:
            path.append(current_pos)
            break

        current_val = triangle[i][current_pos]
        next_row = triangle[i + 1]

        # Check which path leads to the minimum sum
        if current_pos + 1 < len(next_row) and \
           current_sum - current_val == min(next_row[current_pos], next_row[current_pos + 1]):
            path.append(current_pos)
            current_sum -= current_val
            if next_row[current_pos] > next_row[current_pos + 1]:
                current_pos += 1
        else:
            path.append(current_pos)
            current_sum -= current_val

    return path


def test_minimum_total():
    solution = Solution()

    test_cases = [
        {
            "triangle": [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
            "expected": 11,
            "description": "Standard case"
        },
        {
            "triangle": [[-10]],
            "expected": -10,
            "description": "Single element"
        },
        {
            "triangle": [[1], [2, 3], [4, 5, 6]],
            "expected": 7,
            "description": "Small triangle"
        },
        {
            "triangle": [[1], [-5, 2], [3, -2, 4], [-1, 2, -3, 1]],
            "expected": -4,
            "description": "Negative numbers"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        triangle = test_case["triangle"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print("\nTriangle:")
        print_triangle_with_path(triangle)

        # Test all three implementations
        result1 = solution.minimumTotal(triangle)
        result2 = solution.minimumTotalTopDown(triangle)
        result3 = solution.minimumTotal2D(triangle)

        print(f"\nMinimum path sum: {result1}")

        # Find and display the minimum path
        min_path = find_min_path(triangle, result1)
        print("\nMinimum path highlighted:")
        print_triangle_with_path(triangle, min_path)

        assert result1 == expected and result2 == expected and result3 == expected, \
            f"Expected {expected}, but got {result1} (bottom-up), " \
            f"{result2} (top-down), {result3} (2D)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_minimum_total()
    print("\nAll test cases passed! 🎉")
