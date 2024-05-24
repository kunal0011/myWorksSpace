package miscellaneous;

public class KthElementInSpiralOrder {
    public static int findKthElement(int[][] matrix, int k) {
        if (matrix == null || matrix.length == 0 || k <= 0) {
            throw new IllegalArgumentException("Invalid input");
        }

        int rows = matrix.length;
        int cols = matrix[0].length;
        if (k > rows * cols) {
            throw new IllegalArgumentException("k is larger than the number of elements in the matrix");
        }

        int top = 0, bottom = rows - 1;
        int left = 0, right = cols - 1;
        int count = 0;

        while (top <= bottom && left <= right) {
            // Traverse from left to right along the top row
            for (int i = left; i <= right; i++) {
                count++;
                if (count == k) {
                    return matrix[top][i];
                }
            }
            top++;

            // Traverse from top to bottom along the right column
            for (int i = top; i <= bottom; i++) {
                count++;
                if (count == k) {
                    return matrix[i][right];
                }
            }
            right--;

            // Traverse from right to left along the bottom row (if applicable)
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    count++;
                    if (count == k) {
                        return matrix[bottom][i];
                    }
                }
                bottom--;
            }

            // Traverse from bottom to top along the left column (if applicable)
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    count++;
                    if (count == k) {
                        return matrix[i][left];
                    }
                }
                left++;
            }
        }

        throw new IllegalArgumentException("k is out of the bounds of the matrix traversal");
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}
        };

        int k = 10;
        try {
            int kthElement = findKthElement(matrix, k);
            System.out.println("The " + k + "th element in spiral order is: " + kthElement);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}

