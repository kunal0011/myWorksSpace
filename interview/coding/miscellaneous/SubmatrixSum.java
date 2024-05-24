package miscellaneous;

public class SubmatrixSum {
    private int[][] prefixSum;

    public SubmatrixSum(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        prefixSum = new int[rows][cols];

        // Compute the prefix sum array
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                prefixSum[i][j] = matrix[i][j];
                if (i > 0) prefixSum[i][j] += prefixSum[i-1][j];
                if (j > 0) prefixSum[i][j] += prefixSum[i][j-1];
                if (i > 0 && j > 0) prefixSum[i][j] -= prefixSum[i-1][j-1];
            }
        }
    }

    public int querySum(int r1, int c1, int r2, int c2) {
        int sum = prefixSum[r2][c2];
        if (r1 > 0) sum -= prefixSum[r1-1][c2];
        if (c1 > 0) sum -= prefixSum[r2][c1-1];
        if (r1 > 0 && c1 > 0) sum += prefixSum[r1-1][c1-1];
        return sum;
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };

        SubmatrixSum submatrixSum = new SubmatrixSum(matrix);
        System.out.println("Sum of submatrix (1, 1) to (2, 2): " + submatrixSum.querySum(1, 1, 2, 2)); // Output: 28
        System.out.println("Sum of submatrix (0, 0) to (1, 1): " + submatrixSum.querySum(0, 0, 1, 1)); // Output: 12
        System.out.println("Sum of submatrix (1, 0) to (2, 1): " + submatrixSum.querySum(1, 0, 2, 1)); // Output: 24
    }
}
