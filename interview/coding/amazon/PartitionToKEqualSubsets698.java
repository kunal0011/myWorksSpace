package amazon;

import java.util.Arrays;

public class PartitionToKEqualSubsets698 {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int totalSum = Arrays.stream(nums).sum();

        // If the total sum isn't divisible by k, partitioning isn't possible
        if (totalSum % k != 0) {
            return false;
        }

        int targetSum = totalSum / k;
        Arrays.sort(nums);

        // If the largest number is greater than the target sum, partitioning is impossible
        if (nums[nums.length - 1] > targetSum) {
            return false;
        }

        int[] subsetSums = new int[k];
        Arrays.fill(subsetSums, 0);

        // Backtracking function to check if we can partition the array into k subsets
        return backtrack(nums, subsetSums, nums.length - 1, targetSum);
    }

    private boolean backtrack(int[] nums, int[] subsetSums, int index, int targetSum) {
        // If all numbers have been assigned, we successfully partitioned the array
        if (index < 0) {
            return true;
        }

        int currentNum = nums[index];

        // Try to assign the current number to each subset
        for (int i = 0; i < subsetSums.length; i++) {
            if (subsetSums[i] + currentNum <= targetSum) {
                subsetSums[i] += currentNum;
                if (backtrack(nums, subsetSums, index - 1, targetSum)) {
                    return true;
                }
                // Backtrack
                subsetSums[i] -= currentNum;
            }

            // If the current subset is empty, there's no point in continuing with further subsets
            if (subsetSums[i] == 0) {
                break;
            }
        }

        return false;
    }

    // Test the function
    public static void main(String[] args) {
        PartitionToKEqualSubsets698 sol = new PartitionToKEqualSubsets698();

        // Test case 1
        int[] nums1 = {4, 3, 2, 3, 5, 2, 1};
        int k1 = 4;
        System.out.println(sol.canPartitionKSubsets(nums1, k1));  // Output: true

        // Test case 2
        int[] nums2 = {1, 2, 3, 4};
        int k2 = 3;
        System.out.println(sol.canPartitionKSubsets(nums2, k2));  // Output: false
    }
}
