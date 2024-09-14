package amazon;

import java.util.HashMap;
import java.util.Map;

public class KthDistinctString {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> frequencyMap = new HashMap<>();

        // Count frequency of each string
        for (String s : arr) {
            frequencyMap.put(s, frequencyMap.getOrDefault(s, 0) + 1);
        }

        // Iterate over the array and look for the k-th distinct string
        for (String s : arr) {
            if (frequencyMap.get(s) == 1) {
                k--;
                if (k == 0) {
                    return s;
                }
            }
        }

        // If k-th distinct string is not found
        return "";
    }
}
