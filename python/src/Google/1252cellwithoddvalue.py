"""
LeetCode 1252: Cells with Odd Values in a Matrix

Problem Statement:
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each
indices[i] = [ri, ci] represents a 0-based index to the matrix. For each pair of [ri, ci] you should
increment all cells in row ri and all cells in column ci by 1.
Return the number of odd-valued cells in the matrix after applying the increment to all pairs in indices.

Logic:
1. Use two arrays to track increments for rows and columns
2. For each operation in indices:
   - Increment count for the specified row
   - Increment count for the specified column
3. Final value of cell[i][j] = row_count[i] + col_count[j]
4. Count cells where sum is odd

Time Complexity: O(m*n + k) where k is length of indices
Space Complexity: O(m + n) for row and column counts
"""


class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        row_count = [0] * m
        col_count = [0] * n

        # Apply operations to row_count and col_count
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1

        # Count cells with odd values
        odd_cells = 0

        for r in range(m):
            for c in range(n):
                if (row_count[r] + col_count[c]) % 2 == 1:
                    odd_cells += 1

        return odd_cells


def test_odd_cells():
    solution = Solution()

    # Test case 1: Basic case
    m1, n1 = 2, 3
    indices1 = [[0, 1], [1, 1]]
    result1 = solution.oddCells(m1, n1, indices1)
    assert result1 == 6, f"Test case 1 failed. Expected 6, got {result1}"
    print(f"Test case 1 passed: {result1} odd cells")

    # Test case 2: Single operation
    m2, n2 = 2, 2
    indices2 = [[1, 1]]
    result2 = solution.oddCells(m2, n2, indices2)
    assert result2 == 3, f"Test case 2 failed. Expected 3, got {result2}"
    print(f"\nTest case 2 passed: {result2} odd cells")

    # Test case 3: No odd cells
    m3, n3 = 2, 2
    indices3 = [[0, 0], [1, 1]]
    result3 = solution.oddCells(m3, n3, indices3)
    assert result3 == 0, f"Test case 3 failed. Expected 0, got {result3}"
    print(f"\nTest case 3 passed: {result3} odd cells")

    # Test case 4: All cells affected
    m4, n4 = 1, 1
    indices4 = [[0, 0]]
    result4 = solution.oddCells(m4, n4, indices4)
    assert result4 == 1, f"Test case 4 failed. Expected 1, got {result4}"
    print(f"\nTest case 4 passed: {result4} odd cells")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_odd_cells()
