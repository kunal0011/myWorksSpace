package amazon;

import java.util.HashMap;

public class CountwordFormed1160 {
    public int countCharacters(String[] words, String chars) {
        HashMap<Character, Integer> charsCount = new HashMap<>();

        // Count the frequency of each character in 'chars'
        for (char c : chars.toCharArray()) {
            charsCount.put(c, charsCount.getOrDefault(c, 0) + 1);
        }

        int totalLength = 0;

        // Iterate through each word
        for (String word : words) {
            HashMap<Character, Integer> wordCount = new HashMap<>();

            // Count the frequency of each character in the word
            for (char c : word.toCharArray()) {
                wordCount.put(c, wordCount.getOrDefault(c, 0) + 1);
            }

            // Check if we can form the word with 'chars'
            boolean canForm = true;
            for (char c : word.toCharArray()) {
                if (wordCount.get(c) > charsCount.getOrDefault(c, 0)) {
                    canForm = false;
                    break;
                }
            }

            // If we can form the word, add its length to the total
            if (canForm) {
                totalLength += word.length();
            }
        }

        return totalLength;
    }

    // Test cases
    public static void main(String[] args) {
        CountwordFormed1160 sol = new CountwordFormed1160();

        // Test case 1
        String[] words1 = {"cat", "bt", "hat", "tree"};
        String chars1 = "atach";
        int result1 = sol.countCharacters(words1, chars1);
        System.out.println(result1);  // Expected output: 6

        // Test case 2
        String[] words2 = {"hello", "world", "leetcode"};
        String chars2 = "welldonehoneyr";
        int result2 = sol.countCharacters(words2, chars2);
        System.out.println(result2);  // Expected output: 10
    }
}
