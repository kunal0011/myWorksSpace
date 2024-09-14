package amazon;

import java.util.HashMap;
import java.util.Map;

public class CountOfAbsDiffk {
    public int countKDifference(int[] nums, int k) {
        int count = 0;
        // Use a hashmap to store the frequency of numbers
        Map<Integer, Integer> freqMap = new HashMap<>();

        // Iterate through the array
        for (int num : nums) {
            // Check if there's a number with difference k greater than the current num
            count += freqMap.getOrDefault(num - k, 0);
            // Check if there's a number with difference k smaller than the current num
            count += freqMap.getOrDefault(num + k, 0);

            // Update the frequency map
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        return count;
    }
}
