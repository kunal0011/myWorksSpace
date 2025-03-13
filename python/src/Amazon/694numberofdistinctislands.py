"""
LeetCode 694: Number of Distinct Islands

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid 
are surrounded by water.

Two islands are considered to be the same if and only if one island can be translated 
(and not rotated or reflected) to equal the other.

Return the number of distinct islands.
"""

from typing import List, Set

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        distinct_islands = set()
        
        def dfs(r: int, c: int, path: str) -> str:
            if (r < 0 or r >= rows or c < 0 or c >= cols 
                or grid[r][c] == 0):
                return ""
            
            # Mark as visited
            grid[r][c] = 0
            
            # Explore all 4 directions with unique identifiers
            path = (path + 
                   "d" + dfs(r + 1, c, "") +  # down
                   "u" + dfs(r - 1, c, "") +  # up
                   "r" + dfs(r, c + 1, "") +  # right
                   "l" + dfs(r, c - 1, ""))   # left
            return path
        
        # Find all islands and their signatures
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    signature = dfs(r, c, "o")  # 'o' for origin
                    distinct_islands.add(signature)
        
        return len(distinct_islands)

def test_distinct_islands():
    test_cases = [
        {
            'grid': [
                [1,1,0,0,0],
                [1,1,0,0,0],
                [0,0,0,1,1],
                [0,0,0,1,1]
            ],
            'expected': 1
        },
        {
            'grid': [
                [1,1,0,1,1],
                [1,0,0,0,0],
                [0,0,0,0,1],
                [1,1,0,1,1]
            ],
            'expected': 3
        }
    ]
    
    solution = Solution()
    for i, test in enumerate(test_cases, 1):
        # Create a deep copy of grid since it's modified during DFS
        grid_copy = [row[:] for row in test['grid']]
        result = solution.numDistinctIslands(grid_copy)
        print(f"Test case {i}:")
        print(f"Input grid:")
        for row in test['grid']:
            print(row)
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}\n")

if __name__ == "__main__":
    test_distinct_islands()
