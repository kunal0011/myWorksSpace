package amazon;

public class SparseMultiplication311 {
    public int[][] multiply(int[][] mat1, int[][] mat2) {
        int m = mat1.length, k = mat1[0].length, n = mat2[0].length;
        int[][] result = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < k; j++) {
                if (mat1[i][j] != 0) {
                    for (int l = 0; l < n; l++) {
                        if (mat2[j][l] != 0) {
                            result[i][l] += mat1[i][j] * mat2[j][l];
                        }
                    }
                }
            }
        }

        return result;
    }
}
