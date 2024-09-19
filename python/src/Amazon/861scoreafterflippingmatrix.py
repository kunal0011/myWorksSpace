class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Step 1: Ensure that the first column has all 1s
        for i in range(rows):
            if grid[i][0] == 0:  # If the first element in the row is 0, flip the entire row
                for j in range(cols):
                    grid[i][j] ^= 1  # Flip the bit

        # Step 2: Maximize the number of 1s in each column
        for j in range(1, cols):
            count_one = sum(grid[i][j] for i in range(rows))
            if count_one < rows / 2:  # If there are more 0s than 1s, flip the column
                for i in range(rows):
                    grid[i][j] ^= 1  # Flip the bit

        # Step 3: Calculate the final score
        score = 0
        for row in grid:
            # Convert binary row to integer and add to the score
            score += int("".join(map(str, row)), 2)

        return score


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    grid1 = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    print(sol.matrixScore(grid1))  # Expected output: 39

    # Test case 2
    grid2 = [[1]]
    print(sol.matrixScore(grid2))  # Expected output: 1
