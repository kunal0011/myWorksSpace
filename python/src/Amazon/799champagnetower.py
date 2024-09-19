class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize a 2D array to hold the champagne amounts, up to 100 rows
        tower = [[0] * (r + 1) for r in range(101)]
        tower[0][0] = poured  # Pour the champagne into the top glass

        # Traverse each row and distribute the champagne
        for r in range(query_row):
            for c in range(r + 1):
                if tower[r][c] > 1:  # If this glass overflows
                    # The excess amount to spill
                    excess = (tower[r][c] - 1) / 2.0
                    tower[r][c] = 1  # Cap the current glass at 1
                    tower[r + 1][c] += excess  # Left glass in the next row
                    # Right glass in the next row
                    tower[r + 1][c + 1] += excess

        # Return the amount in the query glass, capped at 1
        return min(1, tower[query_row][query_glass])


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    poured1 = 1
    query_row1 = 1
    query_glass1 = 1
    # Expected output: 0.0
    print(sol.champagneTower(poured1, query_row1, query_glass1))

    # Test case 2
    poured2 = 2
    query_row2 = 1
    query_glass2 = 1
    # Expected output: 0.5
    print(sol.champagneTower(poured2, query_row2, query_glass2))

    # Test case 3
    poured3 = 1000000000
    query_row3 = 99
    query_glass3 = 99
    # Expected output: 1.0
    print(sol.champagneTower(poured3, query_row3, query_glass3))
