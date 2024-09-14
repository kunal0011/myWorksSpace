package amazon;

import java.util.HashMap;
import java.util.Map;

public class LargestUniqueNumber1133 {
    public int largestUniqueNumber(int[] A) {
        // Create a frequency map to store the count of each number
        Map<Integer, Integer> count = new HashMap<>();

        // Populate the frequency map
        for (int num : A) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        // Initialize the result as -1 (in case there is no unique number)
        int largestUnique = -1;

        // Iterate over the map and find the largest number that occurs once
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            if (entry.getValue() == 1 && entry.getKey() > largestUnique) {
                largestUnique = entry.getKey();
            }
        }

        return largestUnique;
    }
}

