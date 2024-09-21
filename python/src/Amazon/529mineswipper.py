from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board

        rows, cols = len(board), len(board[0])
        r, c = click

        if board[r][c] == 'M':  # If it's a mine
            board[r][c] = 'X'
            return board

        def count_mines(x, y):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < rows and 0 <= y + dy < cols and board[x + dx][y + dy] == 'M':
                        count += 1
            return count

        def dfs(x, y):
            mine_count = count_mines(x, y)
            if mine_count > 0:
                # Set the count of adjacent mines
                board[x][y] = str(mine_count)
                return
            board[x][y] = 'B'  # Set the cell to 'B'
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'E':
                        dfs(nx, ny)

        dfs(r, c)  # Start DFS from the clicked cell
        return board


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    board = [["E", "E", "E", "E", "E"],
             ["E", "E", "M", "E", "E"],
             ["E", "E", "E", "E", "E"],
             ["E", "E", "E", "E", "E"]]
    click = [3, 0]
    updated_board = sol.updateBoard(board, click)
    for row in updated_board:
        print(row)  # Check the output

    # Test case 2
    board = [["B", "1", "E", "1", "B"],
             ["B", "1", "M", "1", "B"],
             ["B", "1", "1", "1", "B"],
             ["E", "E", "E", "E", "E"]]
    click = [1, 2]
    updated_board = sol.updateBoard(board, click)
    for row in updated_board:
        print(row)  # Check the output
