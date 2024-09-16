package amazon;

import java.util.Arrays;

public class MinOperation1769 {
    public int[] minOperations(String boxes) {
        int n = boxes.length();
        int[] result = new int[n];

        // Left-to-right pass
        int count = 0;  // Count of balls encountered
        int operations = 0;  // Total operations to move balls to the current box
        for (int i = 0; i < n; i++) {
            result[i] += operations;  // Add the current number of operations
            count += boxes.charAt(i) - '0';  // Update the count of balls
            operations += count;  // Increment the operations for the next index
        }

        // Right-to-left pass
        count = 0;
        operations = 0;
        for (int i = n - 1; i >= 0; i--) {
            result[i] += operations;  // Add the current number of operations
            count += boxes.charAt(i) - '0';  // Update the count of balls
            operations += count;  // Increment the operations for the next index
        }

        return result;
    }

    // Testing the solution
    public static void main(String[] args) {
        MinOperation1769 solution = new MinOperation1769();

        // Test case
        String boxes = "110";
        int[] result = solution.minOperations(boxes);
        System.out.println("Minimum operations: " + Arrays.toString(result));  // Expected output: [1, 1, 3]
    }
}

