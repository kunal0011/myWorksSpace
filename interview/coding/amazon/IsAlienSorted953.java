package amazon;

import java.util.HashMap;
import java.util.Map;

public class IsAlienSorted953 {
    public boolean isAlienSorted(String[] words, String order) {
        // Create a mapping of each character in the alien language to its index
        Map<Character, Integer> orderMap = new HashMap<>();
        for (int i = 0; i < order.length(); i++) {
            orderMap.put(order.charAt(i), i);
        }

        // Compare each word with the next one
        for (int i = 0; i < words.length - 1; i++) {
            String word1 = words[i];
            String word2 = words[i + 1];

            // Compare the words letter by letter
            int len = Math.min(word1.length(), word2.length());
            for (int k = 0; k < len; k++) {
                char c1 = word1.charAt(k);
                char c2 = word2.charAt(k);

                if (c1 != c2) {
                    // If the characters are different, check their order in the alien language
                    if (orderMap.get(c1) > orderMap.get(c2)) {
                        return false;  // Words are not in correct order
                    }
                    break;  // If they're in correct order, no need to compare further
                }
            }

            // If all characters are the same but word1 is longer than word2, it's wrong
            if (word1.length() > word2.length()) {
                return false;
            }
        }

        return true;
    }

    // Test cases
    public static void main(String[] args) {
        IsAlienSorted953 sol = new IsAlienSorted953();

        // Test case 1
        String[] words1 = {"hello", "leetcode"};
        String order1 = "hlabcdefgijkmnopqrstuvwxyz";
        System.out.println(sol.isAlienSorted(words1, order1));  // Expected output: True

        // Test case 2
        String[] words2 = {"word", "world", "row"};
        String order2 = "worldabcefghijkmnpqstuvxyz";
        System.out.println(sol.isAlienSorted(words2, order2));  // Expected output: False

        // Test case 3
        String[] words3 = {"apple", "app"};
        String order3 = "abcdefghijklmnopqrstuvwxyz";
        System.out.println(sol.isAlienSorted(words3, order3));  // Expected output: False
    }
}
