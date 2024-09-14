package amazon;

import java.util.HashSet;
import java.util.Set;

public class MaxVowel1456 {
    public int maxVowels(String s, int k) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        int maxVowels = 0;
        int currentVowels = 0;

        // Count vowels in the first window of length k
        for (int i = 0; i < k; i++) {
            if (vowels.contains(s.charAt(i))) {
                currentVowels++;
            }
        }

        maxVowels = currentVowels;

        // Slide the window over the rest of the string
        for (int i = k; i < s.length(); i++) {
            // Remove the character going out of the window
            if (vowels.contains(s.charAt(i - k))) {
                currentVowels--;
            }
            // Add the new character coming into the window
            if (vowels.contains(s.charAt(i))) {
                currentVowels++;
            }

            // Update the maximum vowels count
            maxVowels = Math.max(maxVowels, currentVowels);
        }

        return maxVowels;
    }
}
