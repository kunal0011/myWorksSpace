"""
LeetCode 62. Unique Paths

Problem Statement:
There is a robot on an m x n grid. The robot is initially located at the top-left corner (0, 0).
The robot tries to move to the bottom-right corner (m-1, n-1).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take
to reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From (0,0) to (2,1), there are three paths:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
- 1 <= m, n <= 100
- The answer will be less than or equal to 2 * 10^9
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize dp array with 1s
        # dp[i][j] represents number of unique paths to reach position (i,j)
        dp = [[1] * n for _ in range(m)]

        # Fill dp array
        for i in range(1, m):
            for j in range(1, n):
                # Number of paths to current cell is sum of paths from above and left
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


def print_grid(grid: list, highlight: tuple = None, path: list = None) -> None:
    """Helper function to print grid with optional highlighting and path"""
    m, n = len(grid), len(grid[0])

    # Print column numbers
    print("   ", end="")
    for j in range(n):
        print(f"{j:4}", end=" ")
    print("\n   " + "----" * n)

    for i in range(m):
        print(f"{i:2}|", end=" ")
        for j in range(n):
            if highlight and (i, j) == highlight:
                print(f"\033[92m{grid[i][j]:4}\033[0m", end=" ")
            elif path and (i, j) in path:
                print(f"\033[93m{grid[i][j]:4}\033[0m", end=" ")
            else:
                print(f"{grid[i][j]:4}", end=" ")
        print()
    print()


def explain_unique_paths(m: int, n: int) -> None:
    """
    Function to explain the unique paths calculation process step by step
    """
    print(f"\nCalculating unique paths for {m}x{n} grid")
    print("=" * 50)

    # Initialize dp array
    dp = [[1] * n for _ in range(m)]
    print("\nInitial grid (edges initialized to 1):")
    print_grid(dp)

    # Fill dp array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            print(f"\nCalculating paths to position ({i},{j}):")
            print(f"Paths from above ({i-1},{j}): {dp[i-1][j]}")
            print(f"Paths from left ({i},{j-1}): {dp[i][j-1]}")
            print(f"Total paths to ({i},{j}): {dp[i][j]}")
            print_grid(dp, (i, j))

    print("\nFinal grid showing number of unique paths to each position:")
    print_grid(dp)
    print(f"Number of unique paths to bottom-right corner: {dp[m-1][n-1]}")
    return dp[m-1][n-1]


def test_unique_paths():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "m": 3,
            "n": 7,
            "expected": 28,
            "description": "Basic case"
        },
        {
            "m": 3,
            "n": 2,
            "expected": 3,
            "description": "Small grid"
        },
        {
            "m": 7,
            "n": 3,
            "expected": 28,
            "description": "Transposed grid"
        },
        {
            "m": 1,
            "n": 1,
            "expected": 1,
            "description": "Single cell"
        },
        {
            "m": 2,
            "n": 2,
            "expected": 2,
            "description": "2x2 grid"
        },
        {
            "m": 4,
            "n": 4,
            "expected": 20,
            "description": "Square grid"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        m = test_case["m"]
        n = test_case["n"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: m = {m}, n = {n}")

        result = solution.uniquePaths(m, n)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_unique_paths()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_unique_paths(3, 3)
        explain_unique_paths(3, 7)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
