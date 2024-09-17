package amazon;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class MaxNoOfOccuranceOFSubstring1297 {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
        // Map to count occurrences of substrings
        Map<String, Integer> substringCount = new HashMap<>();

        // Traverse the string with a sliding window of size minSize
        for (int i = 0; i <= s.length() - minSize; i++) {
            // Get the substring of length minSize
            String substring = s.substring(i, i + minSize);

            // Count unique characters in the substring
            HashSet<Character> uniqueChars = new HashSet<>();
            for (char c : substring.toCharArray()) {
                uniqueChars.add(c);
            }

            // Only count the substring if it has <= maxLetters unique characters
            if (uniqueChars.size() <= maxLetters) {
                substringCount.put(substring, substringCount.getOrDefault(substring, 0) + 1);
            }
        }

        // Find the maximum frequency of any valid substring
        int maxFrequency = 0;
        for (int count : substringCount.values()) {
            maxFrequency = Math.max(maxFrequency, count);
        }

        return maxFrequency;
    }

    // Test cases
    public static void main(String[] args) {
        MaxNoOfOccuranceOFSubstring1297 sol = new MaxNoOfOccuranceOFSubstring1297();

        // Test case 1
        String s1 = "aababcaab";
        int maxLetters1 = 2;
        int minSize1 = 3;
        int maxSize1 = 4;
        int result1 = sol.maxFreq(s1, maxLetters1, minSize1, maxSize1);
        assert result1 == 2 : "Test case 1 failed: " + result1;

        // Test case 2
        String s2 = "aaaa";
        int maxLetters2 = 1;
        int minSize2 = 3;
        int maxSize2 = 3;
        int result2 = sol.maxFreq(s2, maxLetters2, minSize2, maxSize2);
        assert result2 == 2 : "Test case 2 failed: " + result2;

        // Test case 3
        String s3 = "abcde";
        int maxLetters3 = 2;
        int minSize3 = 3;
        int maxSize3 = 3;
        int result3 = sol.maxFreq(s3, maxLetters3, minSize3, maxSize3);
        assert result3 == 0 : "Test case 3 failed: " + result3;

        System.out.println("All test cases passed!");
    }
}

