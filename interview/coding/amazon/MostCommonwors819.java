package amazon;

import java.util.*;

public class MostCommonwors819 {
    public String mostCommonWord(String paragraph, String[] banned) {
        // Step 1: Preprocess the paragraph - remove punctuation and make everything lowercase
        String normalizedStr = paragraph.replaceAll("[^a-zA-Z0-9 ]", " ").toLowerCase();
        String[] words = normalizedStr.split("\\s+");

        // Step 2: Create a set of banned words for fast lookup
        Set<String> bannedSet = new HashSet<>(Arrays.asList(banned));

        // Step 3: Count the frequency of each word, excluding banned words
        Map<String, Integer> wordCount = new HashMap<>();
        for (String word : words) {
            if (!bannedSet.contains(word)) {
                wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
            }
        }

        // Step 4: Find the most common word
        return Collections.max(wordCount.entrySet(), Map.Entry.comparingByValue()).getKey();
    }

    // Test cases
    public static void main(String[] args) {
        MostCommonwors819 sol = new MostCommonwors819();

        // Test case 1
        String paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit.";
        String[] banned1 = {"hit"};
        System.out.println(sol.mostCommonWord(paragraph1, banned1));  // Expected output: "ball"

        // Test case 2
        String paragraph2 = "a.";
        String[] banned2 = {};
        System.out.println(sol.mostCommonWord(paragraph2, banned2));  // Expected output: "a"
    }
}
