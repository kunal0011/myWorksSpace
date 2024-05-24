package backtracking;

public class KnightsTour {

    private static final int[] moveX = {2, 1, -1, -2, -2, -1, 1, 2};
    private static final int[] moveY = {1, 2, 2, 1, -1, -2, -2, -1};
    private static final int N = 8; // Example for an 8x8 board

    public static void main(String[] args) {
        solveKnightsTour();
    }

    private static void solveKnightsTour() {
        int[][] board = new int[N][N];

        // Initialize the board with -1
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                board[i][j] = -1;
            }
        }

        // Starting position
        int startX = 0;
        int startY = 0;
        board[startX][startY] = 0; // First move

        if (solveKnightsTourUtil(board, startX, startY, 1)) {
            printSolution(board);
        } else {
            System.out.println("Solution does not exist");
        }
    }

    private static boolean solveKnightsTourUtil(int[][] board, int x, int y, int moveCount) {
        if (moveCount == N * N) {
            return true;
        }

        for (int i = 0; i < 8; i++) {
            int nextX = x + moveX[i];
            int nextY = y + moveY[i];

            if (isSafe(nextX, nextY, board)) {
                board[nextX][nextY] = moveCount;
                if (solveKnightsTourUtil(board, nextX, nextY, moveCount + 1)) {
                    return true;
                } else {
                    board[nextX][nextY] = -1; // backtracking
                }
            }
        }

        return false;
    }

    private static boolean isSafe(int x, int y, int[][] board) {
        return x >= 0 && x < N && y >= 0 && y < N && board[x][y] == -1;
    }

    private static void printSolution(int[][] board) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(board[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
