"""
LeetCode 542 - 01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- mat[i][j] is either 0 or 1
- There is at least one 0 in mat
"""

from collections import deque
from typing import List
import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []

        rows, cols = len(mat), len(mat[0])
        dist = [[math.inf] * cols for _ in range(rows)]
        
        # First pass: check for 0s and initialize queue
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        # Second pass: BFS from all 0s simultaneously
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            curr_dist = dist[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    dist[nr][nc] > curr_dist + 1):
                    dist[nr][nc] = curr_dist + 1
                    queue.append((nr, nc))

        return dist

    def updateMatrix_dp(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Alternative solution using dynamic programming approach
        Time complexity: O(m*n), Space complexity: O(1)
        """
        rows, cols = len(mat), len(mat[0])
        
        # First pass: from top-left to bottom-right
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    top = mat[r-1][c] if r > 0 else math.inf
                    left = mat[r][c-1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        # Second pass: from bottom-right to top-left
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if mat[r][c] != 0:
                    bottom = mat[r+1][c] if r < rows-1 else math.inf
                    right = mat[r][c+1] if c < cols-1 else math.inf
                    mat[r][c] = min(mat[r][c], min(bottom, right) + 1)

        return mat


def test_update_matrix():
    """
    Test function to verify both solution approaches with various test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([[0,0,0],
          [0,1,0],
          [0,0,0]], [[0,0,0],
                     [0,1,0],
                     [0,0,0]]),
        
        ([[0,0,0],
          [0,1,0],
          [1,1,1]], [[0,0,0],
                     [0,1,0],
                     [1,2,1]]),
                     
        # Complex test cases
        ([[1,1,1],
          [1,1,1],
          [1,1,0]], [[4,3,2],
                     [3,2,1],
                     [2,1,0]]),
                     
        # Edge cases
        ([[0]], [[0]]),
        
        ([[1,1],
          [0,1]], [[1,2],
                   [0,1]]),
                   
        # Large distance test
        ([[1,1,1,1],
          [1,1,1,1],
          [1,1,1,0]], [[4,3,2,1],
                       [3,2,1,1],
                       [2,1,1,0]])
    ]
    
    for i, (input_mat, expected) in enumerate(test_cases, 1):
        # Deep copy input for both solutions
        input_bfs = [row[:] for row in input_mat]
        input_dp = [row[:] for row in input_mat]
        
        # Test BFS solution
        result_bfs = solution.updateMatrix(input_bfs)
        # Test DP solution
        result_dp = solution.updateMatrix_dp(input_dp)
        
        bfs_correct = result_bfs == expected
        dp_correct = result_dp == expected
        
        print(f"\nTest Case {i}:")
        print(f"Input matrix:")
        for row in input_mat:
            print(row)
        
        print("\nBFS Solution:", "✓" if bfs_correct else "✗")
        if not bfs_correct:
            print("Got:")
            for row in result_bfs:
                print(row)
            print("Expected:")
            for row in expected:
                print(row)
                
        print("\nDP Solution:", "✓" if dp_correct else "✗")
        if not dp_correct:
            print("Got:")
            for row in result_dp:
                print(row)
            print("Expected:")
            for row in expected:
                print(row)
        
        print("-" * 50)


if __name__ == "__main__":
    test_update_matrix()
