"""
LeetCode 994: Rotting Oranges

You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell
- 1 representing a fresh orange
- 2 representing a rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2
"""

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Queue to hold the positions of all initially rotten oranges
        queue = deque()
        fresh_count = 0

        # Step 1: Add all the initially rotten oranges to the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If there are no fresh oranges, return 0 (no time needed)
        if fresh_count == 0:
            return 0

        # Step 2: BFS to spread the rot
        minutes_passed = 0
        # Right, Down, Left, Up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            minutes_passed += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # Check all 4 directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If the adjacent cell is a fresh orange, rot it and add it to the queue
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Rotten the fresh orange
                        fresh_count -= 1  # Decrease the fresh orange count
                        queue.append((nr, nc))

        # If there are still fresh oranges left, return -1 (not all could rot)
        return minutes_passed - 1 if fresh_count == 0 else -1

def validate_grid(grid: List[List[int]]) -> bool:
    """Validate grid according to constraints"""
    if not grid or not grid[0]:
        return False
    m, n = len(grid), len(grid[0])
    if not (1 <= m <= 10 and 1 <= n <= 10):
        return False
    return all(cell in (0, 1, 2) for row in grid for cell in row)

def visualize_grid(grid: List[List[int]], minute: int = 0) -> None:
    """Visualize grid state at given minute"""
    symbols = {0: '⬜', 1: '🟡', 2: '🟤'}  # Empty, Fresh, Rotten
    print(f"\nMinute {minute}:")
    for row in grid:
        print(''.join(symbols[cell] for cell in row))

def test_rotting_oranges():
    """Test function for Rotting Oranges"""
    test_cases = [
        ([[2,1,1],[1,1,0],[0,1,1]], 4),
        ([[2,1,1],[0,1,1],[1,0,1]], -1),
        ([[0,2]], 0),
        ([[1]], -1),
        ([[2,1,1,1],[1,1,0,1],[0,1,0,1]], 6)
    ]
    
    solution = Solution()
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        # Make deep copy of grid for visualization
        grid_copy = [row[:] for row in grid]
        is_valid = validate_grid(grid)
        
        print(f"\nTest case {i}:")
        print("Initial state:")
        visualize_grid(grid_copy)
        
        result = solution.orangesRotting(grid)
        
        print(f"Minutes required: {result}")
        print(f"Expected: {expected}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Count oranges
        fresh = sum(row.count(1) for row in grid_copy)
        rotten = sum(row.count(2) for row in grid_copy)
        empty = sum(row.count(0) for row in grid_copy)
        
        print("\nGrid statistics:")
        print(f"Dimensions: {len(grid)}x{len(grid[0])}")
        print(f"Fresh oranges: {fresh}")
        print(f"Rotten oranges: {rotten}")
        print(f"Empty cells: {empty}")

if __name__ == "__main__":
    test_rotting_oranges()
