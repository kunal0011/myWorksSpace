package amazon;

import java.util.Arrays;

public class Matrixblocksum1314 {
    public int[][] matrixBlockSum(int[][] mat, int K) {
        int m = mat.length, n = mat[0].length;

        // Step 1: Build the prefix sum matrix
        int[][] prefix = new int[m + 1][n + 1];

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefix[i][j] = mat[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
            }
        }

        // Step 2: Compute the result matrix using the prefix sum matrix
        int[][] result = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Define the bounds for the block
                int r1 = Math.max(0, i - K), c1 = Math.max(0, j - K);
                int r2 = Math.min(m - 1, i + K), c2 = Math.min(n - 1, j + K);

                // Using prefix sum to compute the block sum
                result[i][j] = prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1];
            }
        }

        return result;
    }

    // Testing
    public static void main(String[] args) {
        Matrixblocksum1314 solution = new Matrixblocksum1314();
        int[][] mat = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int K = 1;
        int[][] result = solution.matrixBlockSum(mat, K);
        System.out.println("Java Test Result: ");
        for (int[] row : result) {
            System.out.println(Arrays.toString(row));  // Output: [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
        }
    }
}
