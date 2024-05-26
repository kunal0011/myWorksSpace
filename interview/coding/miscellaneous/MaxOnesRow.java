package miscellaneous;

public class MaxOnesRow {
    public static int findRowWithMaxOnes(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return -1; // If the matrix is empty or invalid, return -1
        }

        int numRows = matrix.length;
        int numCols = matrix[0].length;

        int maxRowIndex = -1;
        int maxOnesCount = -1;

        // Start from the top-right corner of the matrix
        int row = 0, col = numCols - 1;

        while (row < numRows && col >= 0) {
            if (matrix[row][col] == 1) {
                // Move left if the current element is 1
                col--;
                maxRowIndex = row; // Update the row index with max 1s
            } else {
                // Move down if the current element is 0
                row++;
            }
        }

        return maxRowIndex;
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {0, 0, 0, 1},
                {0, 1, 1, 1},
                {1, 1, 1, 1},
                {0, 0, 0, 0}
        };
        int result = findRowWithMaxOnes(matrix);
        System.out.println("The row with the maximum number of 1s is: " + result); // Output: 2
    }
}
