from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):

            l = []

            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif board[i][j] not in l:
                    l.append(board[i][j])
                else:
                    return False

        for i in range(9):

            l = []

            for j in range(9):
                if board[j][i] == '.':
                    continue

                elif board[j][i] not in l:

                    l.append(board[j][i])
                else:

                    return False

        for i in range(0, 9, 3):

            for j in range(0, 9, 3):
                l = []
                for k1 in range(i, i+3):
                    for k in range(j, j+3):
                        if board[k1][k] == '.':
                            continue
                        elif board[k1][k] not in l:

                            l.append(board[k1][k])
                        else:

                            return False

        return True


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    box_index = (r // 3) * 3 + (c // 3)

                    if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                        return False

                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

        return True


if __name__ == '__main__':

    s = Solution()

    print(s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [

        "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(s.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
          "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(s.isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."], [
          ".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."], [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
