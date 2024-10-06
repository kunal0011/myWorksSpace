from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track rows, columns, and 3x3 sub-boxes
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        # Iterate over every cell in the board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                # Calculate box index based on the row and column indices
                box_index = (i // 3) * 3 + (j // 3)

                # Check if the number is already present in the row, column, or box
                if num in row_sets[i] or num in col_sets[j] or num in box_sets[box_index]:
                    return False

                # Add the number to the respective row, column, and box sets
                row_sets[i].add(num)
                col_sets[j].add(num)
                box_sets[box_index].add(num)

        return True
