"""
LeetCode 529 - Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:
- 'M' represents an unrevealed mine
- 'E' represents an unrevealed empty square
- 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals)
- digit ('1' to '8') represents how many mines are adjacent to this revealed square
- 'X' represents a revealed mine

You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:
1. If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
2. If an empty square 'E' with no adjacent mines is revealed, then change it to 'B' and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square 'E' with at least one adjacent mine is revealed, then change it to the number of adjacent mines.
4. Return the board when no more squares will be revealed.

Example 1:
Input: board = [["E","E","E","E","E"],
               ["E","E","M","E","E"],
               ["E","E","E","E","E"],
               ["E","E","E","E","E"]], 
       click = [3,0]
Output: [["B","1","E","1","B"],
         ["B","1","M","1","B"],
         ["B","1","1","1","B"],
         ["B","B","B","B","B"]]
"""

from typing import List
from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]:
            return board

        rows, cols = len(board), len(board[0])
        row, col = click
        
        # If we click on a mine, game over
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
            
        def count_adjacent_mines(r: int, c: int) -> int:
            """Helper function to count adjacent mines"""
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    new_r, new_c = r + dr, c + dc
                    if (0 <= new_r < rows and 
                        0 <= new_c < cols and 
                        board[new_r][new_c] == 'M'):
                        count += 1
            return count

        def dfs(r: int, c: int):
            """DFS to reveal squares"""
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'E':
                return
                
            mines = count_adjacent_mines(r, c)
            if mines == 0:
                board[r][c] = 'B'
                # Recursively reveal adjacent squares
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        dfs(r + dr, c + dc)
            else:
                board[r][c] = str(mines)

        # Start DFS from click position
        if board[row][col] == 'E':
            dfs(row, col)
            
        return board

    def updateBoard_bfs(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """Alternative solution using BFS approach"""
        if not board or not board[0]:
            return board

        rows, cols = len(board), len(board[0])
        row, col = click
        
        # If we click on a mine, game over
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
            
        def count_adjacent_mines(r: int, c: int) -> int:
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    new_r, new_c = r + dr, c + dc
                    if (0 <= new_r < rows and 
                        0 <= new_c < cols and 
                        board[new_r][new_c] == 'M'):
                        count += 1
            return count

        # BFS approach
        queue = deque([(row, col)])
        visited = {(row, col)}

        while queue:
            r, c = queue.popleft()
            if board[r][c] != 'E':
                continue
                
            mines = count_adjacent_mines(r, c)
            if mines == 0:
                board[r][c] = 'B'
                # Add adjacent squares to queue
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        new_r, new_c = r + dr, c + dc
                        if (0 <= new_r < rows and 
                            0 <= new_c < cols and 
                            (new_r, new_c) not in visited and 
                            board[new_r][new_c] == 'E'):
                            queue.append((new_r, new_c))
                            visited.add((new_r, new_c))
            else:
                board[r][c] = str(mines)
                
        return board


def test_minesweeper():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        # Test case 1: Basic example from problem statement
        (
            [["E","E","E","E","E"],
             ["E","E","M","E","E"],
             ["E","E","E","E","E"],
             ["E","E","E","E","E"]],
            [3,0],
            [["B","1","E","1","B"],
             ["B","1","M","1","B"],
             ["B","1","1","1","B"],
             ["B","B","B","B","B"]]
        ),
        # Test case 2: Click on mine
        (
            [["E","E","E"],
             ["E","M","E"],
             ["E","E","E"]],
            [1,1],
            [["E","E","E"],
             ["E","X","E"],
             ["E","E","E"]]
        ),
        # Test case 3: Click on number
        (
            [["E","E","E"],
             ["E","M","E"],
             ["E","E","E"]],
            [0,0],
            [["1","E","E"],
             ["E","M","E"],
             ["E","E","E"]]
        ),
        # Test case 4: Multiple mines
        (
            [["E","E","E","E"],
             ["E","M","M","E"],
             ["E","E","E","E"],
             ["E","E","E","E"]],
            [0,0],
            [["1","2","2","1"],
             ["E","M","M","E"],
             ["E","E","E","E"],
             ["E","E","E","E"]]
        ),
        # Test case 5: Single cell board
        (
            [["M"]],
            [0,0],
            [["X"]]
        )
    ]
    
    for i, (board, click, expected) in enumerate(test_cases, 1):
        # Create copies of the board for each solution
        board_dfs = [row[:] for row in board]
        board_bfs = [row[:] for row in board]
        
        # Test DFS solution
        result_dfs = solution.updateBoard(board_dfs, click)
        # Test BFS solution
        result_bfs = solution.updateBoard_bfs(board_bfs, click)
        
        dfs_correct = result_dfs == expected
        bfs_correct = result_bfs == expected
        
        print(f"Test {i}:")
        print("Input Board:")
        for row in board:
            print(row)
        print(f"Click: {click}")
        print("\nDFS Solution:")
        for row in result_dfs:
            print(row)
        print(f"DFS Result: {'✓' if dfs_correct else '✗'}")
        print("\nBFS Solution:")
        for row in result_bfs:
            print(row)
        print(f"BFS Result: {'✓' if bfs_correct else '✗'}")
        print("\nExpected:")
        for row in expected:
            print(row)
        print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    test_minesweeper()