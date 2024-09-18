package amazon;

import java.util.Arrays;

public class LargestsumofArraywithknegation1005 {
    public int largestSumAfterKNegations(int[] nums, int K) {
        // Sort the array to prioritize the smallest elements for negation
        Arrays.sort(nums);

        // Negate the negative elements as much as we can
        for (int i = 0; i < nums.length && K > 0; i++) {
            if (nums[i] < 0) {
                nums[i] = -nums[i];
                K--;
            }
        }

        // If K is still odd, we need to negate the smallest element again
        Arrays.sort(nums);  // Re-sort to find the smallest element
        if (K % 2 == 1) {
            nums[0] = -nums[0];
        }

        // Return the sum of the array
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum;
    }

    // Testing
    public static void main(String[] args) {
        LargestsumofArraywithknegation1005 solution = new LargestsumofArraywithknegation1005();
        int[] nums = {4, 2, 3};
        int K = 1;
        System.out.println("Java Test Result: " + solution.largestSumAfterKNegations(nums, K));  // Output: 5
    }
}

