from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:
                # All queens are placed, add the solution to the results
                result.append(["".join(board[i]) for i in range(n)])
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place the queen
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to the next row
                backtrack(row + 1)

                # Backtrack: remove the queen and try next column
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        result = []
        board = [['.'] * n for _ in range(n)]
        cols = set()  # Columns where queens are placed
        diag1 = set()  # Diagonals with slope \ where queens are placed
        diag2 = set()  # Diagonals with slope / where queens are placed

        backtrack(0)
        return result


# Example usage
solution = Solution()
n = 4
print(solution.solveNQueens(n))
