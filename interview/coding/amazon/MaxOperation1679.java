package amazon;

import java.util.HashMap;

public class MaxOperation1679 {
    public int maxOperations(int[] nums, int k) {
        HashMap<Integer, Integer> countMap = new HashMap<>();
        int operations = 0;

        for (int num : nums) {
            int complement = k - num;
            if (countMap.getOrDefault(complement, 0) > 0) {
                operations++;
                countMap.put(complement, countMap.get(complement) - 1);  // Use up the complement
            } else {
                countMap.put(num, countMap.getOrDefault(num, 0) + 1);  // Store the current number
            }
        }

        return operations;
    }

    // Testing the solution
    public static void main(String[] args) {
        MaxOperation1679 solution = new MaxOperation1679();

        // Test cases
        int[] nums1 = {1, 2, 3, 4};
        int k1 = 5;
        System.out.println("Max number of k-sum pairs: " + solution.maxOperations(nums1, k1));  // Expected output: 2

        int[] nums2 = {3, 1, 3, 4, 3};
        int k2 = 6;
        System.out.println("Max number of k-sum pairs: " + solution.maxOperations(nums2, k2));  // Expected output: 1
    }
}

