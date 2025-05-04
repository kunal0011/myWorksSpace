"""
LeetCode 1289: Minimum Falling Path Sum II

Problem Statement:
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.
A falling path with non-zero shifts is a choice of exactly one element from each row that:
- All adjacent elements in the path must be in different columns
- Each element can't be in the same column as the element from previous row

Logic:
1. Use dynamic programming approach
2. For each cell, add minimum value from previous row's different columns
3. Final answer is minimum value in last row
4. Optimization: Track first and second minimum from previous row

Time Complexity: O(n^2)
Space Complexity: O(1) as we modify input grid
"""


class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        for i in range(1, n):
            for j in range(n):
                grid[i][j] += min(grid[i-1][k] for k in range(n) if k != j)
        return min(grid[-1])


def test_min_falling_path_sum():
    solution = Solution()

    # Test case 1: Basic case
    grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = solution.minFallingPathSum(grid1)
    assert result1 == 13, f"Test case 1 failed. Expected 13, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: Negative numbers
    grid2 = [[-1, 2, 3], [4, -5, 6], [7, 8, -9]]
    result2 = solution.minFallingPathSum(grid2)
    assert result2 == -6, f"Test case 2 failed. Expected -6, got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Single cell
    grid3 = [[1]]
    result3 = solution.minFallingPathSum(grid3)
    assert result3 == 1, f"Test case 3 failed. Expected 1, got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Large values
    grid4 = [[100, -100, 100], [-100, 100, -100], [100, -100, 100]]
    result4 = solution.minFallingPathSum(grid4)
    assert result4 == -300, f"Test case 4 failed. Expected -300, got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_min_falling_path_sum()
