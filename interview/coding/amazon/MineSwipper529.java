package amazon;

public class MineSwipper529 {
    int[][] directions = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

    public char[][] updateBoard(char[][] board, int[] click) {
        int rows = board.length;
        int cols = board[0].length;
        int r = click[0], c = click[1];

        if (board[r][c] == 'M') {  // If it's a mine
            board[r][c] = 'X';
            return board;
        }

        // Directions for 8 adjacent cells

        // Count adjacent mines




        dfs(r, c,board,rows,cols);  // Start DFS from the clicked cell
        return board;
    }
    void dfs(int x, int y, char[][] board, int rows, int cols) {
        int mineCount = countMines(x, y,rows,cols,board);
        if (mineCount > 0) {
            board[x][y] = (char) ('0' + mineCount);  // Set the count of adjacent mines
            return;
        }
        board[x][y] = 'B';  // Set the cell to 'B'
        for (int[] d : directions) {
            int nx = x + d[0], ny = y + d[1];
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && board[nx][ny] == 'E') {
                dfs(nx, ny, board, rows, cols);
            }
        }
    }
    int countMines(int x, int y, int rows, int cols, char[][] board) {
        int count = 0;
        for (int[] d : directions) {
            int nx = x + d[0], ny = y + d[1];
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols && board[nx][ny] == 'M') {
                count++;
            }
        }
        return count;
    }
    // Test cases
    public static void main(String[] args) {
        MineSwipper529 sol = new MineSwipper529();

        // Test case 1
        char[][] board1 = {
                {'E', 'E', 'E', 'E', 'E'},
                {'E', 'E', 'M', 'E', 'E'},
                {'E', 'E', 'E', 'E', 'E'},
                {'E', 'E', 'E', 'E', 'E'}
        };
        int[] click1 = {3, 0};
        char[][] updatedBoard1 = sol.updateBoard(board1, click1);
        for (char[] row : updatedBoard1) {
            System.out.println(row);
        }

        // Test case 2
        char[][] board2 = {
                {'B', '1', 'E', '1', 'B'},
                {'B', '1', 'M', '1', 'B'},
                {'B', '1', '1', '1', 'B'},
                {'E', 'E', 'E', 'E', 'E'}
        };
        int[] click2 = {1, 2};
        char[][] updatedBoard2 = sol.updateBoard(board2, click2);
        for (char[] row : updatedBoard2) {
            System.out.println(row);
        }
    }
}

