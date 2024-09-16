package amazon;

public class Rotatefunction396 {
    public int maxRotateFunction(int[] nums) {
        int n = nums.length;
        int totalSum = 0, F_0 = 0;

        // Compute totalSum and F(0)
        for (int i = 0; i < n; i++) {
            totalSum += nums[i];
            F_0 += i * nums[i];
        }

        int max_value = F_0;
        int current_F = F_0;

        // Compute subsequent F(k) for k = 1 to n-1
        for (int k = 1; k < n; k++) {
            current_F += totalSum - n * nums[n - k];
            max_value = Math.max(max_value, current_F);
        }

        return max_value;
    }

    // Test the solution
    public static void main(String[] args) {
        Rotatefunction396 sol = new Rotatefunction396();

        // Test case 1: Example from Leetcode
        int[] nums1 = {4, 3, 2, 6};
        System.out.println(sol.maxRotateFunction(nums1));  // Expected output: 26

        // Test case 2: All elements are the same
        int[] nums2 = {100, 100, 100};
        System.out.println(sol.maxRotateFunction(nums2));  // Expected output: 0

        // Test case 3: Array of length 1
        int[] nums3 = {1};
        System.out.println(sol.maxRotateFunction(nums3));  // Expected output: 0
    }
}
