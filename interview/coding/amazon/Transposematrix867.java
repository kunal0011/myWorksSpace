package amazon;

public class Transposematrix867 {
    public int[][] transpose(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] result = new int[cols][rows];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result[j][i] = matrix[i][j];
            }
        }

        return result;
    }

    // Test cases
    public static void main(String[] args) {
        Transposematrix867 sol = new Transposematrix867();

        // Test case 1
        int[][] matrix1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int[][] result1 = sol.transpose(matrix1);
        for (int[] row : result1) {
            System.out.println(java.util.Arrays.toString(row));  // Expected output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        }

        // Test case 2
        int[][] matrix2 = {{1, 2, 3}, {4, 5, 6}};
        int[][] result2 = sol.transpose(matrix2);
        for (int[] row : result2) {
            System.out.println(java.util.Arrays.toString(row));  // Expected output: [[1, 4], [2, 5], [3, 6]]
        }
    }
}
