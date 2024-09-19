package amazon;

public class MaxIncreaseTokeepcityskylineclean807 {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int n = grid.length;

        // Step 1: Find the maximum heights for each row and each column
        int[] maxRow = new int[n];
        int[] maxCol = new int[n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                maxRow[i] = Math.max(maxRow[i], grid[i][j]);
                maxCol[j] = Math.max(maxCol[j], grid[i][j]);
            }
        }

        // Step 2: Calculate the total possible increase
        int totalIncrease = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                totalIncrease += Math.min(maxRow[i], maxCol[j]) - grid[i][j];
            }
        }

        return totalIncrease;
    }

    // Test cases
    public static void main(String[] args) {
        MaxIncreaseTokeepcityskylineclean807 sol = new MaxIncreaseTokeepcityskylineclean807();

        // Test case 1
        int[][] grid1 = {
                {3, 0, 8, 4},
                {2, 4, 5, 7},
                {9, 2, 6, 3},
                {0, 3, 1, 0}
        };
        System.out.println(sol.maxIncreaseKeepingSkyline(grid1));  // Expected output: 35

        // Test case 2
        int[][] grid2 = {
                {0, 0, 0},
                {0, 0, 0},
                {0, 0, 0}
        };
        System.out.println(sol.maxIncreaseKeepingSkyline(grid2));  // Expected output: 0
    }
}
