package amazon;

import java.util.*;

public class ShortEncodingOfWords820 {
    public int minimumLengthEncoding(String[] words) {
        Set<String> wordSet = new HashSet<>(Arrays.asList(words));

        // Remove any word that is a suffix of another word
        for (String word : words) {
            for (int k = 1; k < word.length(); ++k) {
                wordSet.remove(word.substring(k));
            }
        }

        int result = 0;
        // Add the length of each remaining word + 1 (for the # character)
        for (String word : wordSet) {
            result += word.length() + 1;
        }

        return result;
    }

    // Test cases
    public static void main(String[] args) {
        ShortEncodingOfWords820 sol = new ShortEncodingOfWords820();

        // Test case 1
        String[] words1 = {"time", "me", "bell"};
        System.out.println(sol.minimumLengthEncoding(words1));  // Expected output: 10 ("time#bell#")

        // Test case 2
        String[] words2 = {"t"};
        System.out.println(sol.minimumLengthEncoding(words2));  // Expected output: 2 ("t#")
    }
}
