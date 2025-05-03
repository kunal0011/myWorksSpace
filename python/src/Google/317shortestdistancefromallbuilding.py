"""
LeetCode 317 - Shortest Distance from All Buildings

Problem Statement:
You are given an m x n grid of values 0, 1, or 2, where:
- 0 represents an empty cell that we can pass through
- 1 represents a building
- 2 represents an obstacle that we cannot pass through
Your task is to find a vacant land cell (0) having the shortest total distance to all buildings (1).
Return -1 if it's impossible to build the house.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|
"""

from collections import deque
from typing import List

def shortestDistance(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    total_buildings = sum(cell == 1 for row in grid for cell in row)
    distances = [[0] * cols for _ in range(rows)]
    reach_count = [[0] * cols for _ in range(rows)]
    
    def bfs(row: int, col: int, building_id: int) -> None:
        visited = set()
        queue = deque([(row, col, 0)])
        visited.add((row, col))
        
        while queue:
            curr_row, curr_col, dist = queue.popleft()
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_col = curr_row + dx, curr_col + dy
                
                if (0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    grid[new_row][new_col] == 0 and 
                    (new_row, new_col) not in visited):
                    
                    distances[new_row][new_col] += dist + 1
                    reach_count[new_row][new_col] += 1
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, dist + 1))
    
    # Perform BFS from each building
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                bfs(i, j, total_buildings)
    
    # Find the minimum distance among all valid empty cells
    min_distance = float('inf')
    for i in range(rows):
        for j in range(cols):
            if (grid[i][j] == 0 and 
                reach_count[i][j] == total_buildings and 
                distances[i][j] < min_distance):
                min_distance = distances[i][j]
    
    return min_distance if min_distance != float('inf') else -1

# Test driver
def run_tests():
    test_cases = [
        (
            [
                [1,0,2,0,1],
                [0,0,0,0,0],
                [0,0,1,0,0]
            ],
            7
        ),
        (
            [
                [1,0],
                [0,0]
            ],
            1
        ),
        (
            [
                [1,2,0]
            ],
            -1
        )
    ]
    
    for i, (grid, expected) in enumerate(test_cases, 1):
        result = shortestDistance(grid)
        print(f"\nTest case {i}:")
        print(f"Input grid:")
        for row in grid:
            print(row)
        print(f"Expected output: {expected}")
        print(f"Actual output: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")

if __name__ == "__main__":
    run_tests() 