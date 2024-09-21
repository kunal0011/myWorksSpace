package amazon;

public class DetectCapital520 {
    public boolean detectCapitalUse(String word) {
        // Case 1: All letters are capitals
        if (word.equals(word.toUpperCase())) {
            return true;
        }

        // Case 2: All letters are lowercase
        if (word.equals(word.toLowerCase())) {
            return true;
        }

        // Case 3: Only the first letter is capitalized and the rest are lowercase
        if (Character.isUpperCase(word.charAt(0)) && word.substring(1).equals(word.substring(1).toLowerCase())) {
            return true;
        }

        // If none of the conditions are met, return False
        return false;
    }

    // Test cases
    public static void main(String[] args) {
        DetectCapital520 sol = new DetectCapital520();

        // Test case 1
        String word1 = "USA";
        System.out.println(sol.detectCapitalUse(word1));  // Expected output: True

        // Test case 2
        String word2 = "leetcode";
        System.out.println(sol.detectCapitalUse(word2));  // Expected output: True

        // Test case 3
        String word3 = "Google";
        System.out.println(sol.detectCapitalUse(word3));  // Expected output: True

        // Test case 4
        String word4 = "FlaG";
        System.out.println(sol.detectCapitalUse(word4));  // Expected output: False
    }
}
