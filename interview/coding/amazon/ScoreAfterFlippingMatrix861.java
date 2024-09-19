package amazon;

public class ScoreAfterFlippingMatrix861 {
    public int matrixScore(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;

        // Step 1: Ensure that the first column has all 1s
        for (int i = 0; i < rows; i++) {
            if (grid[i][0] == 0) {
                // Flip the row if the first element is 0
                for (int j = 0; j < cols; j++) {
                    grid[i][j] ^= 1;
                }
            }
        }

        // Step 2: Maximize the number of 1s in each column
        for (int j = 1; j < cols; j++) {
            int countOne = 0;
            for (int i = 0; i < rows; i++) {
                countOne += grid[i][j];
            }
            if (countOne < rows / 2) {
                // If there are more 0s than 1s, flip the column
                for (int i = 0; i < rows; i++) {
                    grid[i][j] ^= 1;
                }
            }
        }

        // Step 3: Calculate the final score
        int score = 0;
        for (int i = 0; i < rows; i++) {
            int rowValue = 0;
            for (int j = 0; j < cols; j++) {
                rowValue = (rowValue << 1) + grid[i][j];
            }
            score += rowValue;
        }

        return score;
    }

    // Test cases
    public static void main(String[] args) {
        ScoreAfterFlippingMatrix861 sol = new ScoreAfterFlippingMatrix861();

        // Test case 1
        int[][] grid1 = {{0,0,1,1},{1,0,1,0},{1,1,0,0}};
        System.out.println(sol.matrixScore(grid1));  // Expected output: 39

        // Test case 2
        int[][] grid2 = {{1}};
        System.out.println(sol.matrixScore(grid2));  // Expected output: 1
    }
}
