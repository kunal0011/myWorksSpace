package amazon;

public class MaxAbsoluteSum1749 {
    public int maxAbsoluteSum(int[] nums) {
        int maxSum = 0;
        int minSum = 0;
        int currentMax = 0;
        int currentMin = 0;

        for (int num : nums) {
            currentMax = Math.max(currentMax + num, num);
            maxSum = Math.max(maxSum, currentMax);

            currentMin = Math.min(currentMin + num, num);
            minSum = Math.min(minSum, currentMin);
        }

        return Math.max(Math.abs(maxSum), Math.abs(minSum));
    }

    // Testing the solution
    public static void main(String[] args) {
        MaxAbsoluteSum1749 solution = new MaxAbsoluteSum1749();

        // Test case
        int[] nums = {1, -3, 2, 3, -4};
        System.out.println("Maximum absolute sum: " + solution.maxAbsoluteSum(nums));  // Expected output: 5
    }
}
