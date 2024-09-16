package amazon;

public class Longestprefix1392 {
    public String longestPrefix(String s) {
        // KMP algorithm to find the longest prefix which is also suffix
        int n = s.length();
        int[] lps = new int[n];  // Longest Prefix Suffix array
        int length = 0;  // Length of the previous longest prefix suffix
        int i = 1;

        // Build the LPS array
        while (i < n) {
            if (s.charAt(i) == s.charAt(length)) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) {
                    length = lps[length - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }

        return s.substring(0, lps[n - 1]);
    }

    // Test cases
    public static void main(String[] args) {
        Longestprefix1392 sol = new Longestprefix1392();

        // Test 1
        String s1 = "level";
        assert sol.longestPrefix(s1).equals("l") : "Test case 1 failed";

        // Test 2
        String s2 = "ababab";
        assert sol.longestPrefix(s2).equals("abab") : "Test case 2 failed";

        // Test 3
        String s3 = "leetcodeleet";
        assert sol.longestPrefix(s3).equals("leet") : "Test case 3 failed";

        System.out.println("All test cases passed!");
    }
}

