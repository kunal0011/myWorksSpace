from typing import List

"""
LeetCode 64. Minimum Path Sum

Problem Statement:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Path is: 1 → 3 → 1 → 1 → 1 = 7

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 100
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # Initialize first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Initialize first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Fill dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]


def print_grids(grid: List[List[int]], dp: List[List[int]],
                current: tuple = None, path: List[tuple] = None) -> None:
    """Helper function to print both original grid and dp array"""
    m, n = len(grid), len(grid[0])

    print("Original Grid:")
    for i in range(m):
        for j in range(n):
            if current and (i, j) == current:
                print(f"\033[92m{grid[i][j]:2}\033[0m", end=" ")
            elif path and (i, j) in path:
                print(f"\033[93m{grid[i][j]:2}\033[0m", end=" ")
            else:
                print(f"{grid[i][j]:2}", end=" ")
        print()

    print("\nMinimum Path Sums:")
    for i in range(m):
        for j in range(n):
            if current and (i, j) == current:
                print(f"\033[92m{dp[i][j]:2}\033[0m", end=" ")
            elif path and (i, j) in path:
                print(f"\033[93m{dp[i][j]:2}\033[0m", end=" ")
            else:
                print(f"{dp[i][j]:2}", end=" ")
        print()
    print()


def explain_min_path_sum(grid: List[List[int]]) -> None:
    """
    Function to explain the minimum path sum calculation process step by step
    """
    print(f"\nCalculating minimum path sum:")
    print("=" * 50)

    if not grid:
        print("Empty grid!")
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize start position
    dp[0][0] = grid[0][0]
    print("\nInitializing start position:")
    print_grids(grid, dp, (0, 0))

    # Initialize first row
    print("\nInitializing first row:")
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
        print(f"Position (0,{j}):")
        print_grids(grid, dp, (0, j))

    # Initialize first column
    print("\nInitializing first column:")
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        print(f"Position ({i},0):")
        print_grids(grid, dp, (i, 0))

    # Fill dp array
    print("\nFilling remaining positions:")
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            print(f"\nCalculating minimum path to ({i},{j}):")
            print(f"Value at current position: {grid[i][j]}")
            print(f"Path sum from above ({i-1},{j}): {dp[i-1][j]}")
            print(f"Path sum from left ({i},{j-1}): {dp[i][j-1]}")
            print(f"Minimum path sum: {dp[i][j]}")
            print_grids(grid, dp, (i, j))

    # Find the actual path
    path = [(m-1, n-1)]
    i, j = m-1, n-1
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if dp[i-1][j] < dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        elif i > 0:
            i -= 1
        else:
            j -= 1
        path.append((i, j))

    print("\nFinal result with minimum path highlighted:")
    print_grids(grid, dp, path=path[::-1])
    print(f"Minimum path sum: {dp[m-1][n-1]}")
    return dp[m-1][n-1]


def test_min_path_sum():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "grid": [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
            "expected": 7,
            "description": "Basic case"
        },
        {
            "grid": [[1, 2, 3], [4, 5, 6]],
            "expected": 12,
            "description": "2x3 grid"
        },
        {
            "grid": [[1]],
            "expected": 1,
            "description": "Single cell"
        },
        {
            "grid": [[1, 2], [1, 1]],
            "expected": 3,
            "description": "2x2 grid"
        },
        {
            "grid": [[9, 1, 4], [9, 1, 5], [1, 1, 1]],
            "expected": 5,
            "description": "Path with detour"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        grid = test_case["grid"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print("Input grid:")
        for row in grid:
            print(row)

        result = solution.minPathSum(grid)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_min_path_sum()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        explain_min_path_sum([[1, 2, 3], [4, 5, 6]])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
