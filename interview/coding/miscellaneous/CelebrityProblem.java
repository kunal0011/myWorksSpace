package miscellaneous;

public class CelebrityProblem {

    // Function to check if person i knows person j
    private static boolean knows(int[][] matrix, int i, int j) {
        return matrix[i][j] == 1;
    }

    // Function to find the celebrity
    public static int findCelebrity(int[][] matrix) {
        int n = matrix.length;
        int left = 0;
        int right = n - 1;

        // Two pointer approach
        while (left < right) {
            if (knows(matrix, left, right)) {
                left++; // left cannot be the celebrity
            } else {
                right--; // right cannot be the celebrity
            }
        }

        // Check if the potential celebrity (left) knows no one and is known by everyone else
        for (int i = 0; i < n; i++) {
            if (i != left && (knows(matrix, left, i) || !knows(matrix, i, left))) {
                return -1; // No celebrity found
            }
        }

        return left; // Celebrity found
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {0, 0, 1, 0},
                {0, 0, 1, 0},
                {0, 0, 0, 0},
                {0, 0, 1, 0}
        };

        int celebrity = findCelebrity(matrix);
        if (celebrity != -1) {
            System.out.println("Celebrity found at index: " + celebrity);
        } else {
            System.out.println("No celebrity found");
        }
    }
}

