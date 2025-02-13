from typing import List


class Solution:
    """
    LeetCode 200 - Number of Islands

    Problem Statement:
    Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water),
    return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or
    vertically. You may assume all four edges of the grid are all surrounded by water.

    Example:
    Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    Output: 3
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS Solution

        Logic:
        1. Iterate through each cell in the grid
        2. When we find a '1', increment island count and explore the entire island
        3. Mark visited cells as '0' to avoid counting them again

        Time Complexity: O(m*n) where m,n are grid dimensions
        Space Complexity: O(m*n) in worst case for DFS stack
        """
        if not grid:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> None:
            # Check bounds and if current cell is land
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                    grid[row][col] == "0"):
                return

            # Mark current cell as visited
            grid[row][col] = "0"

            # Explore all 4 directions
            dfs(row+1, col)  # down
            dfs(row-1, col)  # up
            dfs(row, col+1)  # right
            dfs(row, col-1)  # left

        # Iterate through each cell in grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands

    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        """
        BFS Solution

        Time Complexity: O(m*n)
        Space Complexity: O(min(m,n)) for queue
        """
        if not grid:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(row: int, col: int) -> None:
            queue = [(row, col)]
            grid[row][col] = "0"  # Mark as visited

            while queue:
                curr_row, curr_col = queue.pop(0)

                # Check all 4 directions
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r, c = curr_row + dr, curr_col + dc
                    if (0 <= r < rows and
                        0 <= c < cols and
                            grid[r][c] == "1"):
                        queue.append((r, c))
                        grid[r][c] = "0"  # Mark as visited

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)

        return islands


def run_tests():
    """Test driver for Number of Islands solutions"""
    solution = Solution()

    test_cases = [
        {
            'grid': [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"]
            ],
            'expected': 3,
            'explanation': "3 islands: 2x2 island, single cell island, and 2x1 island"
        },
        {
            'grid': [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"]
            ],
            'expected': 1,
            'explanation': "1 island connected horizontally and vertically"
        },
        {
            'grid': [["1"]],
            'expected': 1,
            'explanation': "Single cell grid with land"
        },
        {
            'grid': [["0"]],
            'expected': 0,
            'explanation': "Single cell grid with water"
        }
    ]

    methods = [
        ('DFS Solution', solution.numIslands),
        ('BFS Solution', solution.numIslands_bfs)
    ]

    for method_name, method in methods:
        print(f"\nTesting {method_name}:")
        print("-" * 50)

        for i, test in enumerate(test_cases, 1):
            # Create a deep copy of grid since we modify it
            grid_copy = [row[:] for row in test['grid']]
            result = method(grid_copy)
            passed = result == test['expected']

            print(f"Test {i}:")
            print("Input grid:")
            for row in test['grid']:
                print(row)
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")
            print(f"Explanation: {test['explanation']}")
            print(f"Result: {'✓ PASS' if passed else '✗ FAIL'}\n")


if __name__ == "__main__":
    run_tests()
