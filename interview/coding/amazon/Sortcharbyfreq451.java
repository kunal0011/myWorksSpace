package amazon;

import java.util.*;

public class Sortcharbyfreq451 {
    public String frequencySort(String s) {
        // Step 1: Count the frequency of each character
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }

        // Step 2: Sort characters by frequency in descending order
        List<Character> chars = new ArrayList<>(freqMap.keySet());
        Collections.sort(chars, (a, b) -> freqMap.get(b) - freqMap.get(a));

        // Step 3: Build the result string
        StringBuilder result = new StringBuilder();
        for (char c : chars) {
            int count = freqMap.get(c);
            for (int i = 0; i < count; i++) {
                result.append(c);
            }
        }

        return result.toString();
    }

    // Test cases
    public static void main(String[] args) {
        Sortcharbyfreq451 sol = new Sortcharbyfreq451();

        // Test case 1
        String s1 = "tree";
        System.out.println(sol.frequencySort(s1));  // Expected output: "eert" or "eetr"

        // Test case 2
        String s2 = "cccaaa";
        System.out.println(sol.frequencySort(s2));  // Expected output: "cccaaa" or "aaaccc"

        // Test case 3
        String s3 = "Aabb";
        System.out.println(sol.frequencySort(s3));  // Expected output: "bbAa" or "bbaA"
    }
}

