"""
LeetCode 417 - Pacific Atlantic Water Flow

Problem Statement:
-----------------
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches 
the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer 
matrix heights where heights[r][c] represents the height above sea level of the cell at 
coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells 
directly north, south, east, and west if the neighboring cell's height is less than or 
equal to the current cell's height. Water can flow from any cell adjacent to an ocean 
into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain 
water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Key Points:
----------
1. Water flows from higher or equal height to lower height
2. Pacific Ocean is at top and left edges
3. Atlantic Ocean is at bottom and right edges
4. Need to find cells that can reach both oceans
5. Use DFS or BFS from ocean edges inward (reverse flow approach)

Examples:
--------
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]

Constraints:
-----------
* m == heights.length
* n == heights[r].length
* 1 <= m, n <= 200
* 0 <= heights[r][c] <= 10^5
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Find cells from which water can flow to both Pacific and Atlantic oceans.
        Uses DFS approach starting from ocean edges and working inward.
        
        Time Complexity: O(M*N) where M and N are dimensions of the grid
        Space Complexity: O(M*N) for visited arrays
        """
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic_reachable = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r: int, c: int, reachable: List[List[bool]]) -> None:
            """
            Depth-first search to mark cells reachable from current position.
            Water flows from higher/equal heights to lower heights.
            """
            reachable[r][c] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < rows and 0 <= new_c < cols and 
                    not reachable[new_r][new_c] and 
                    heights[new_r][new_c] >= heights[r][c]):
                    dfs(new_r, new_c, reachable)

        # Process ocean edges
        for r in range(rows):
            dfs(r, 0, pacific_reachable)      # Pacific (left edge)
            dfs(r, cols - 1, atlantic_reachable)  # Atlantic (right edge)

        for c in range(cols):
            dfs(0, c, pacific_reachable)      # Pacific (top edge)
            dfs(rows - 1, c, atlantic_reachable)  # Atlantic (bottom edge)

        # Find cells reachable from both oceans
        return [[r, c] for r in range(rows) for c in range(cols) 
                if pacific_reachable[r][c] and atlantic_reachable[r][c]]


def test_pacific_atlantic():
    """
    Test driver for the Pacific Atlantic Water Flow problem
    """
    test_cases = [
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4]
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        ),
        (
            [[2, 1], [1, 2]],
            [[0, 0], [0, 1], [1, 0], [1, 1]]
        ),
        (
            [[1]],
            [[0, 0]]
        ),
        (
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
            [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        ),
    ]
    
    solution = Solution()
    
    for i, (heights, expected) in enumerate(test_cases, 1):
        result = solution.pacificAtlantic(heights)
        # Sort both lists for consistent comparison
        result.sort()
        expected.sort()
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input matrix:")
        for row in heights:
            print(row)
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_pacific_atlantic()
