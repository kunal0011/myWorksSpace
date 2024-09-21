package amazon;

import java.util.Arrays;

public class Validtriangle611 {
    public int triangleNumber(int[] nums) {
        // Sort the array
        Arrays.sort(nums);
        int count = 0;
        int n = nums.length;

        // Fix the third side and use two pointers for the other two
        for (int k = 2; k < n; k++) {
            int i = 0, j = k - 1;
            while (i < j) {
                if (nums[i] + nums[j] > nums[k]) {
                    count += j - i;  // All pairs (i, j), (i, j-1), ..., (i, i+1) are valid
                    j--;  // Move j left to find more pairs
                } else {
                    i++;  // Move i right to find a valid pair
                }
            }
        }

        return count;
    }

    // Test cases
    public static void main(String[] args) {
        Validtriangle611 sol = new Validtriangle611();

        // Test case 1
        int[] nums1 = {2, 2, 3, 4};
        System.out.println(sol.triangleNumber(nums1));  // Output: 3

        // Test case 2
        int[] nums2 = {4, 2, 3, 4};
        System.out.println(sol.triangleNumber(nums2));  // Output: 4
    }
}

