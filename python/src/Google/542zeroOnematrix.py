"""
LeetCode 542 - 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Logic:
1. Initialize a distance matrix with infinity for all cells
2. Add all cells with value 0 to a queue with distance 0
3. Use BFS to update distances:
   - For each cell in queue, check its 4 adjacent neighbors
   - If a neighbor's current distance is greater than current cell's distance + 1,
     update it and add to queue
4. The final matrix will have shortest distance to nearest 0 for each cell

Time Complexity: O(m*n) where m,n are dimensions of matrix
Space Complexity: O(m*n) for the distance matrix and queue
"""

from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []

        rows, cols = len(mat), len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        # Step 1: Initialize the queue with all '0' cells
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        # Step 2: BFS to update distances
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    # If new distance is smaller, update and add to queue
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr, nc))

        return dist


def run_test_cases():
    solution = Solution()
    test_cases = [
        {
            "matrix": [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ],
            "expected": [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ],
            "explanation": "The cell at (1,1) has distance 1 to nearest 0"
        },
        {
            "matrix": [
                [0, 0, 0],
                [0, 1, 0],
                [1, 1, 1]
            ],
            "expected": [
                [0, 0, 0],
                [0, 1, 0],
                [1, 2, 1]
            ],
            "explanation": "The cells at (2,0) and (2,2) have distance 1, (2,1) has distance 2"
        },
        {
            "matrix": [[0], [1]],
            "expected": [[0], [1]],
            "explanation": "Single column matrix"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.updateMatrix(test["matrix"])
        print(f"\nTest Case {i}:")
        print("Input Matrix:")
        for row in test["matrix"]:
            print(row)
        print("\nExpected Output:")
        for row in test["expected"]:
            print(row)
        print("\nActual Output:")
        for row in result:
            print(row)
        print(f"Explanation: {test['explanation']}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}")


if __name__ == "__main__":
    run_test_cases()
