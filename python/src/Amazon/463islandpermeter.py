class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Add 4 for the current land cell
                    perimeter += 4

                    # Subtract 2 if there's land below
                    if r < rows - 1 and grid[r + 1][c] == 1:
                        perimeter -= 2

                    # Subtract 2 if there's land to the right
                    if c < cols - 1 and grid[r][c + 1] == 1:
                        perimeter -= 2

        return perimeter


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    grid1 = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]
    print(sol.islandPerimeter(grid1))  # Expected output: 16

    # Test case 2
    grid2 = [
        [1]
    ]
    print(sol.islandPerimeter(grid2))  # Expected output: 4

    # Test case 3
    grid3 = [
        [1, 1],
        [1, 1]
    ]
    print(sol.islandPerimeter(grid3))  # Expected output: 8
