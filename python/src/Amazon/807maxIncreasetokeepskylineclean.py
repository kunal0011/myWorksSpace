class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        # Step 1: Find the maximum heights for each row and each column
        max_row = [max(row) for row in grid]
        max_col = [max(col) for col in zip(*grid)]

        # Step 2: Calculate the total possible increase
        total_increase = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # The new height is constrained by both the row and column maximums
                total_increase += min(max_row[i], max_col[j]) - grid[i][j]

        return total_increase


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    grid1 = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    print(sol.maxIncreaseKeepingSkyline(grid1))  # Expected output: 35

    # Test case 2
    grid2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(sol.maxIncreaseKeepingSkyline(grid2))  # Expected output: 0
