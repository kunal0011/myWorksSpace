package amazon;

import java.util.HashMap;
import java.util.Map;

public class Kdiffinarray532 {
    public int findPairs(int[] nums, int k) {
        if (k < 0) {
            return 0;  // The absolute difference can't be negative, so no pairs can be found.
        }

        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        int count = 0;

        if (k == 0) {
            // If k == 0, we're looking for duplicates, i.e., numbers that appear at least twice
            for (int num : freq.keySet()) {
                if (freq.get(num) > 1) {
                    count++;
                }
            }
        } else {
            // If k > 0, we need to check if num + k exists for each unique num
            for (int num : freq.keySet()) {
                if (freq.containsKey(num + k)) {
                    count++;
                }
            }
        }

        return count;
    }

    // Test case
    public static void main(String[] args) {
        Kdiffinarray532 sol = new Kdiffinarray532();

        // Test case 1
        int[] nums1 = {3, 1, 4, 1, 5};
        int k1 = 2;
        System.out.println(sol.findPairs(nums1, k1));  // Expected output: 2

        // Test case 2
        int[] nums2 = {1, 2, 3, 4, 5};
        int k2 = 1;
        System.out.println(sol.findPairs(nums2, k2));  // Expected output: 4

        // Test case 3
        int[] nums3 = {1, 3, 1, 5, 4};
        int k3 = 0;
        System.out.println(sol.findPairs(nums3, k3));  // Expected output: 1
    }
}

