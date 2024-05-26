package miscellaneous;

import java.util.HashMap;
import java.util.Map;

public class     LargestSubarrayWithEqual01 {

    public static int findMaxLength(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int maxLen = 0;
        int count = 0;
        map.put(0, -1); // Initialize the map with difference 0 at index -1

        for (int i = 0; i < nums.length; i++) {
            // Increment count for 1 and decrement for 0
            count += (nums[i] == 1) ? 1 : -1;

            if (map.containsKey(count)) {
                // If the difference was seen before, calculate the length of the subarray
                maxLen = Math.max(maxLen, i - map.get(count));
            } else {
                // Store the first occurrence of the difference
                map.put(count, i);
            }
        }

        return maxLen;
    }

    public static void main(String[] args) {
        int[] nums = {0, 1, 0, 0, 1, 1, 0};
        System.out.println("Length of largest subarray with equal 0s and 1s: " + findMaxLength(nums)); // Output: 6
    }
}
