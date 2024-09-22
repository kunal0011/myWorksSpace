package amazon;

import java.util.HashMap;

public class Longestpalindrome409 {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> charCount = new HashMap<>();

        // Count occurrences of each character
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }

        int length = 0;
        boolean oddFound = false;

        for (int count : charCount.values()) {
            if (count % 2 == 0) {
                length += count;  // Add even counts directly
            } else {
                length += count - 1;  // Add largest even part of odd counts
                oddFound = true;  // Remember that we found an odd count
            }
        }

        if (oddFound) {
            length += 1;  // Add one more for the center of the palindrome
        }

        return length;
    }

    public static void main(String[] args) {
        Longestpalindrome409 sol = new Longestpalindrome409();
        System.out.println(sol.longestPalindrome("abccccdd"));  // Expected output: 7
        System.out.println(sol.longestPalindrome("a"));          // Expected output: 1
        System.out.println(sol.longestPalindrome("aaabbbccc"));  // Expected output: 7
    }
}

