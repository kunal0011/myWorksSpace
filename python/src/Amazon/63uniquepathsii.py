from typing import List

"""
LeetCode 63. Unique Paths II

Problem Statement:
You are given an m x n integer array obstacleGrid. There is a robot initially located at the 
top-left corner (0, 0). The robot tries to move to the bottom-right corner (m-1, n-1).
The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in obstacleGrid. A path that the robot
takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two paths to the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is 0 or 1
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # Initialize first cell
        dp[0][0] = 1

        # Initialize first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]

        # Initialize first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]

        # Fill dp array
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


def print_grid(grid: List[List[int]], dp: List[List[int]], highlight: tuple = None) -> None:
    """Helper function to print both obstacle grid and dp array"""
    m, n = len(grid), len(grid[0])

    print("Obstacle Grid:")
    for i in range(m):
        for j in range(n):
            if highlight and (i, j) == highlight:
                print(f"\033[92m{grid[i][j]}\033[0m", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()

    print("\nPaths Grid:")
    for i in range(m):
        for j in range(n):
            if highlight and (i, j) == highlight:
                print(f"\033[92m{dp[i][j]:2}\033[0m", end=" ")
            else:
                print(f"{dp[i][j]:2}", end=" ")
        print()
    print()


def explain_unique_paths_with_obstacles(obstacleGrid: List[List[int]]) -> None:
    """
    Function to explain the unique paths calculation process with obstacles
    """
    print(f"\nCalculating unique paths with obstacles:")
    print("=" * 50)

    if not obstacleGrid or obstacleGrid[0][0] == 1:
        print("Start position is blocked or grid is empty!")
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]

    # Initialize first cell
    dp[0][0] = 1
    print("\nInitializing start position:")
    print_grid(obstacleGrid, dp, (0, 0))

    # Initialize first row
    print("\nInitializing first row:")
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j-1]
        print(f"Position (0,{j}):")
        print_grid(obstacleGrid, dp, (0, j))

    # Initialize first column
    print("\nInitializing first column:")
    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
        print(f"Position ({i},0):")
        print_grid(obstacleGrid, dp, (i, 0))

    # Fill dp array
    print("\nFilling remaining positions:")
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                print(f"\nCalculating paths to ({i},{j}):")
                print(f"Paths from above ({i-1},{j}): {dp[i-1][j]}")
                print(f"Paths from left ({i},{j-1}): {dp[i][j-1]}")
                print(f"Total paths: {dp[i][j]}")
                print_grid(obstacleGrid, dp, (i, j))

    print(f"\nFinal number of unique paths: {dp[m-1][n-1]}")
    return dp[m-1][n-1]


def test_unique_paths_with_obstacles():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "grid": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
            "expected": 2,
            "description": "Basic case with center obstacle"
        },
        {
            "grid": [[0, 1], [0, 0]],
            "expected": 1,
            "description": "Simple path with obstacle"
        },
        {
            "grid": [[1, 0]],
            "expected": 0,
            "description": "Blocked start"
        },
        {
            "grid": [[0, 0], [0, 1]],
            "expected": 0,
            "description": "Blocked end"
        },
        {
            "grid": [[0]],
            "expected": 1,
            "description": "Single cell"
        },
        {
            "grid": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            "expected": 6,
            "description": "No obstacles"
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

        result = solution.uniquePathsWithObstacles(grid)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_unique_paths_with_obstacles()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        explain_unique_paths_with_obstacles([[0, 1], [0, 0]])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
