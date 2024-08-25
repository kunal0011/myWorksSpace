class Solution:
    def placeWordInCrossword(self, board, word):
        rows, cols = len(board), len(board[0])
        length = len(word)

        def canPlaceHorizontally(row, col):
            # Ensure word fits in the row
            if col + length > cols:
                return False
            if col > 0 and board[row][col - 1] != '#':  # No adjacent left space
                return False
            # No adjacent right space
            if col + length < cols and board[row][col + length] != '#':
                return False
            for i in range(length):
                if board[row][col + i] not in [' ', word[i]]:
                    return False
            return True

        def canPlaceVertically(row, col):
            # Ensure word fits in the column
            if row + length > rows:
                return False
            if row > 0 and board[row - 1][col] != '#':  # No adjacent upper space
                return False
            # No adjacent lower space
            if row + length < rows and board[row + length][col] != '#':
                return False
            for i in range(length):
                if board[row + i][col] not in [' ', word[i]]:
                    return False
            return True

        def canPlaceHorizontallyReversed(row, col):
            if col - length + 1 < 0:
                return False
            if col < cols - 1 and board[row][col + 1] != '#':
                return False
            if col - length >= 0 and board[row][col - length] != '#':
                return False
            for i in range(length):
                if board[row][col - i] not in [' ', word[i]]:
                    return False
            return True

        def canPlaceVerticallyReversed(row, col):
            if row - length + 1 < 0:
                return False
            if row < rows - 1 and board[row + 1][col] != '#':
                return False
            if row - length >= 0 and board[row - length][col] != '#':
                return False
            for i in range(length):
                if board[row - i][col] not in [' ', word[i]]:
                    return False
            return True

        # Check each position for horizontal, vertical, and their reverse placements
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ' ' or board[r][c] == word[0]:
                    if canPlaceHorizontally(r, c) or canPlaceHorizontallyReversed(r, c):
                        return True
                    if canPlaceVertically(r, c) or canPlaceVerticallyReversed(r, c):
                        return True
        return False


# Example usage
solution = Solution()
board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]]
word = "abc"
print(solution.placeWordInCrossword(board, word))  # Output: True
