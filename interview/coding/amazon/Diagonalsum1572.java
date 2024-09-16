package amazon;

public class Diagonalsum1572 {
    public int diagonalSum(int[][] mat) {
        int n = mat.length;
        int totalSum = 0;

        for (int i = 0; i < n; i++) {
            // Add primary diagonal element
            totalSum += mat[i][i];
            // Add secondary diagonal element
            totalSum += mat[i][n - 1 - i];
        }

        // If the matrix has an odd size, subtract the middle element (it was counted twice)
        if (n % 2 == 1) {
            totalSum -= mat[n / 2][n / 2];
        }

        return totalSum;
    }

    // Testing
    public static void main(String[] args) {
        Diagonalsum1572 solution = new Diagonalsum1572();
        int[][] mat = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };
        System.out.println("Java Test Result: " + solution.diagonalSum(mat));  // Output should be 25
    }
}

