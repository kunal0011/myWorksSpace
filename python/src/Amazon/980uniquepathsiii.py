"""
LeetCode 980: Unique Paths III

You are given an m x n integer array grid where:
- 1 represents the starting square
- 2 represents the ending square
- 0 represents empty squares we can walk through
- -1 represents obstacles we cannot walk through

Return the number of 4-directional walks from start to end, that walk over every 
non-obstacle square exactly once.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 20
- 1 <= m * n <= 20
- -1 <= grid[i][j] <= 2
- There is exactly one starting cell and one ending cell
"""

from typing import List, Set, Tuple
from time import perf_counter

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        empty = 0
        
        # Find start and count walkable squares
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] >= 0:  # Count walkable squares
                    empty += 1
                    
        def dfs(x: int, y: int, remaining: int) -> int:
            if grid[x][y] == 2:  # Reached end
                return 1 if remaining == 1 else 0
                
            paths = 0
            original = grid[x][y]
            grid[x][y] = -1  # Mark as visited
            
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1):
                    paths += dfs(nx, ny, remaining - 1)
                    
            grid[x][y] = original  # Restore original value
            return paths
            
        return dfs(start[0], start[1], empty)

def validate_grid(grid: List[List[int]]) -> bool:
    """Validate grid according to constraints"""
    if not grid or not grid[0]:
        return False
    m, n = len(grid), len(grid[0])
    if not (1 <= m <= 20 and 1 <= n <= 20 and m * n <= 20):
        return False
    
    start_count = end_count = 0
    for row in grid:
        if not all(-1 <= x <= 2 for x in row):
            return False
        start_count += row.count(1)
        end_count += row.count(2)
    return start_count == 1 and end_count == 1

def visualize_path(grid: List[List[int]], path: List[Tuple[int, int]] = None) -> None:
    """Visualize grid and path if provided"""
    symbols = {-1: '▩', 0: '·', 1: 'S', 2: 'E'}
    m, n = len(grid), len(grid[0])
    
    for i in range(m):
        row = ""
        for j in range(n):
            if path and (i, j) in path:
                row += "* "
            else:
                row += symbols[grid[i][j]] + " "
        print(row)

def test_unique_paths():
    """Test function for Unique Paths III"""
    test_cases = [
        ([[1,0,0,0],[0,0,0,0],[0,0,2,-1]], 2),
        ([[1,0,0,0],[0,0,0,0],[0,0,0,2]], 4),
        ([[0,1],[2,0]], 0),
        ([[1,0,2]], 1),
        ([[1,-1,2]], 0)
    ]
    
    solution = Solution()
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        is_valid = validate_grid(grid)
        
        print(f"\nTest case {i}:")
        print("Grid configuration:")
        visualize_path(grid)
        
        start_time = perf_counter()
        result = solution.uniquePathsIII(grid)
        end_time = perf_counter()
        
        print(f"\nNumber of unique paths: {result}")
        print(f"Expected paths: {expected}")
        print(f"Time taken: {(end_time - start_time)*1000:.3f}ms")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        obstacles = sum(row.count(-1) for row in grid)
        walkable = len(grid) * len(grid[0]) - obstacles
        print(f"\nGrid statistics:")
        print(f"Dimensions: {len(grid)}x{len(grid[0])}")
        print(f"Walkable squares: {walkable}")
        print(f"Obstacles: {obstacles}")

if __name__ == "__main__":
    test_unique_paths()
