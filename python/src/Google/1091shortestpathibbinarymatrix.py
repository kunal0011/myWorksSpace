"""
LeetCode 1091: Shortest Path in Binary Matrix

Problem Statement:
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (0, 0) to the bottom-right cell (n-1, n-1) such that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected.
The length of a clear path is the number of visited cells of this path.

Logic:
1. Use BFS (Breadth First Search) to find shortest path
2. Check if start and end points are valid (both must be 0)
3. Move in all 8 directions from each cell:
   - horizontal, vertical, and diagonal moves allowed
   - only move to cells containing 0
4. Mark visited cells to avoid cycles
5. Track path length while traversing

Time Complexity: O(N^2) where N is the dimension of the grid
Space Complexity: O(N^2) for the queue in worst case
"""

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        # If start or end is blocked, return -1
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        # Directions for moving in 8 possible ways
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]

        # Initialize the BFS queue
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark as visited by setting the value to 1

        while queue:
            r, c, path_length = queue.popleft()

            # If we reached the bottom-right corner
            if r == n-1 and c == n-1:
                return path_length

            # Explore all 8 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, path_length + 1))
                    grid[nr][nc] = 1  # Mark the cell as visited

        # If there's no valid path, return -1
        return -1


def test_shortest_path():
    solution = Solution()

    # Test case 1: Basic path exists
    grid1 = [[0, 1, 1],
             [1, 0, 0],
             [1, 1, 0]]
    result1 = solution.shortestPathBinaryMatrix(grid1)
    assert result1 == 3, f"Test case 1 failed. Expected 3, got {result1}"
    print(f"Test case 1 passed: shortest path length = {result1}")

    # Test case 2: No path exists
    grid2 = [[1, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    result2 = solution.shortestPathBinaryMatrix(grid2)
    assert result2 == -1, f"Test case 2 failed. Expected -1, got {result2}"
    print(f"\nTest case 2 passed: no path exists")

    # Test case 3: Single cell grid
    grid3 = [[0]]
    result3 = solution.shortestPathBinaryMatrix(grid3)
    assert result3 == 1, f"Test case 3 failed. Expected 1, got {result3}"
    print(f"\nTest case 3 passed: single cell path")

    # Test case 4: End cell blocked
    grid4 = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 1]]
    result4 = solution.shortestPathBinaryMatrix(grid4)
    assert result4 == -1, f"Test case 4 failed. Expected -1, got {result4}"
    print(f"\nTest case 4 passed: end cell blocked")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_shortest_path()
