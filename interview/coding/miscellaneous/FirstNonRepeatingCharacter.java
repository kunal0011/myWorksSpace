package miscellaneous;

import java.util.HashMap;
import java.util.Map;

public class FirstNonRepeatingCharacter {

    public static char firstNonRepeatingChar(String s) {
        // Map to store character frequency
        Map<Character, Integer> frequencyMap = new HashMap<>();

        // Count frequency of each character
        for (char c : s.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }

        // Find first non-repeating character
        for (char c : s.toCharArray()) {
            if (frequencyMap.get(c) == 1) {
                return c;
            }
        }

        // If no non-repeating character found, return a default value
        return '\0';
    }

    public static void main(String[] args) {
        String input = "leetcode";
        char firstNonRepeating = firstNonRepeatingChar(input);
        System.out.println("First non-repeating character: " + firstNonRepeating); // Output: 'l'
    }
}
