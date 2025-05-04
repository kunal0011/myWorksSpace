"""
LeetCode 1765. Map of Highest Peak

Problem Statement:
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.
- If isWater[i][j] == 0, cell (i, j) is a land cell.
- If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign heights to the land cells such that:
- The height of each cell must be non-negative.
- If the cell is next to water or another land cell, the height difference must be at most 1.
- All water cells must have a height of 0.
Return an matrix result of size m x n where result[i][j] is the height of cell (i, j).

Time Complexity: O(m*n) where m and n are dimensions of the matrix
Space Complexity: O(m*n) for the result matrix and queue
"""

from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # Logic:
        # 1. Use BFS starting from all water cells (height 0)
        # 2. For each cell, process its neighbors:
        #    - If neighbor's height is not set (infinity), set it to current + 1
        #    - Add neighbor to queue for further processing
        # 3. BFS ensures minimum height difference of 1 between adjacent cells

        m, n = len(isWater), len(isWater[0])
        result = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        # Initialize BFS with all water cells
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    queue.append((i, j))

        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Perform BFS
        while queue:
            x, y = queue.popleft()
            current_height = result[x][y]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if result[nx][ny] > current_height + 1:
                        result[nx][ny] = current_height + 1
                        queue.append((nx, ny))

        return result


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [[0, 1], [0, 0]],  # Expected: [[1,0], [2,1]]
        # Expected: [[1,1,0], [0,1,1], [1,2,2]]
        [[0, 0, 1], [1, 0, 0], [0, 0, 0]],
        # Expected: [[0,1,2], [1,2,3], [2,3,4]]
        [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    ]

    for i, isWater in enumerate(test_cases):
        print(f"Test case {i + 1}:")
        print("Input (1=water, 0=land):")
        for row in isWater:
            print(row)

        result = solution.highestPeak(isWater)
        print("\nOutput (heights):")
        for row in result:
            print(row)

        # Verify constraints
        m, n = len(result), len(result[0])
        valid = True
        # Check water cells have height 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1 and result[i][j] != 0:
                    valid = False
                    print(
                        f"Invalid: Water cell at ({i},{j}) has non-zero height")

        # Check adjacent cells differ by at most 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        if abs(result[i][j] - result[ni][nj]) > 1:
                            valid = False
                            print(
                                f"Invalid: Adjacent cells ({i},{j}) and ({ni},{nj}) differ by more than 1")

        print(f"All constraints satisfied: {valid}\n")
