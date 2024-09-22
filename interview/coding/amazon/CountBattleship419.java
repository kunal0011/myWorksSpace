package amazon;

public class CountBattleship419 {
    public int countBattleships(char[][] board) {
        if (board == null || board.length == 0) {
            return 0;
        }

        int rows = board.length;
        int cols = board[0].length;
        int count = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                // Count a battleship only if:
                // - The current cell is 'X'
                // - There is no 'X' above or to the left of it
                if (board[r][c] == 'X') {
                    if ((r == 0 || board[r - 1][c] != 'X') && (c == 0 || board[r][c - 1] != 'X')) {
                        count++;
                    }
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        CountBattleship419 sol = new CountBattleship419();

        // Test case 1
        char[][] board1 = {
                {'X', '.', '.', 'X'},
                {'.', '.', '.', 'X'},
                {'.', '.', '.', 'X'}
        };
        System.out.println(sol.countBattleships(board1));  // Expected output: 2

        // Test case 2
        char[][] board2 = {
                {'X', 'X', 'X', 'X'},
                {'.', '.', '.', '.'},
                {'X', 'X', '.', 'X'}
        };
        System.out.println(sol.countBattleships(board2));  // Expected output: 3
    }
}

