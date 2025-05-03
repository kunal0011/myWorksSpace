"""
LeetCode 417 - Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the 
island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix 
heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly 
north, south, east, and west if the neighboring cell's height is less than or equal to the 
current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water 
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
"""

from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        def dfs(row: int, col: int, visited: Set[Tuple[int, int]], prev_height: int) -> None:
            # Check bounds and if current height is less than previous (water can't flow uphill)
            if (row < 0 or col < 0 or row >= m or col >= n or
                (row, col) in visited or heights[row][col] < prev_height):
                return
            
            visited.add((row, col))
            
            # Check all four directions
            for next_row, next_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                dfs(next_row, next_col, visited, heights[row][col])
        
        # Sets to store cells that can reach each ocean
        pacific = set()
        atlantic = set()
        
        # Check cells on top and bottom edges
        for col in range(n):
            dfs(0, col, pacific, heights[0][col])           # Top edge (Pacific)
            dfs(m-1, col, atlantic, heights[m-1][col])      # Bottom edge (Atlantic)
        
        # Check cells on left and right edges
        for row in range(m):
            dfs(row, 0, pacific, heights[row][0])           # Left edge (Pacific)
            dfs(row, n-1, atlantic, heights[row][n-1])      # Right edge (Atlantic)
        
        # Return coordinates that can reach both oceans
        return [[row, col] for row, col in pacific & atlantic]


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        [[1,2,2,3,5],
         [3,2,3,4,4],
         [2,4,5,3,1],
         [6,7,1,4,5],
         [5,1,1,2,4]],  # Should return [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        
        [[2,1],
         [1,2]],        # Should return [[0,0],[0,1],[1,0],[1,1]]
        
        [[1]],         # Should return [[0,0]]
        
        [[1,2,3],
         [8,9,4],
         [7,6,5]]      # Should return [[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    ]
    
    for heights in test_cases:
        result = solution.pacificAtlantic(heights)
        print(f"\nInput: heights = {heights}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()