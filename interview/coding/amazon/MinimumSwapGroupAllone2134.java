package amazon;

public class MinimumSwapGroupAllone2134 {
    public int minSwaps(int[] nums) {
        int n = nums.length;
        int totalOnes = 0;

        // Count total number of 1's
        for (int num : nums) {
            totalOnes += num;
        }

        if (totalOnes == 0) return 0; // No 1's, no swaps needed

        // Double the array to handle the circular nature
        int[] extendedNums = new int[2 * n];
        for (int i = 0; i < 2 * n; i++) {
            extendedNums[i] = nums[i % n];
        }

        // Initial window: count the number of 1's in the first window of size totalOnes
        int currentOnes = 0;
        for (int i = 0; i < totalOnes; i++) {
            currentOnes += extendedNums[i];
        }

        int maxOnesInWindow = currentOnes;

        // Sliding window: move through the array and update the window
        for (int i = 1; i < n; i++) {
            currentOnes = currentOnes + extendedNums[i + totalOnes - 1] - extendedNums[i - 1];
            maxOnesInWindow = Math.max(maxOnesInWindow, currentOnes);
        }

        // Minimum swaps needed
        return totalOnes - maxOnesInWindow;
    }

    // Test the solution
    public static void main(String[] args) {
        MinimumSwapGroupAllone2134 sol = new MinimumSwapGroupAllone2134();

        // Test case 1: Example from Leetcode
        int[] nums1 = {1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1};
        System.out.println(sol.minSwaps(nums1));  // Expected output: 3

        // Test case 2: No 1's in the array
        int[] nums2 = {0, 0, 0, 0};
        System.out.println(sol.minSwaps(nums2));  // Expected output: 0

        // Test case 3: All 1's in the array
        int[] nums3 = {1, 1, 1, 1};
        System.out.println(sol.minSwaps(nums3));  // Expected output: 0
    }
}
