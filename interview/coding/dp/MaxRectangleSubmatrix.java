package dp;

import java.util.Stack;

public class MaxRectangleSubmatrix {
    public static int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m][n];
        int maxArea = 0;

        // Initialize the first row of the dp matrix
        for (int j = 0; j < n; j++) {
            dp[0][j] = matrix[0][j] - '0';
            maxArea = Math.max(maxArea, dp[0][j]);
        }

        // Fill the dp matrix
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    dp[i][j] = dp[i-1][j] + 1;
                }
            }
        }

        // Calculate the area of the largest rectangle
        for (int i = 0; i < m; i++) {
            maxArea = Math.max(maxArea, largestRectangleArea(dp[i]));
        }

        return maxArea;
    }

    private static int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        int i = 0;
        while (i < heights.length) {
            if (stack.isEmpty() || heights[stack.peek()] <= heights[i]) {
                stack.push(i++);
            } else {
                int top = stack.pop();
                maxArea = Math.max(maxArea, heights[top] * (stack.isEmpty() ? i : i - stack.peek() - 1));
            }
        }
        while (!stack.isEmpty()) {
            int top = stack.pop();
            maxArea = Math.max(maxArea, heights[top] * (stack.isEmpty() ? heights.length : heights.length - stack.peek() - 1));
        }
        return maxArea;
    }

    public static void main(String[] args) {
        char[][] matrix = {
                {'1', '0', '1', '0', '0'},
                {'1', '0', '1', '1', '1'},
                {'1', '1', '1', '1', '1'},
                {'1', '0', '0', '1', '0'}
        };
        System.out.println("Maximum size of rectangular submatrix with all 1s: " + maximalRectangle(matrix)); // Output: 6
    }
}

