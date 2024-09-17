package amazon;


public class IncreasingDecreasingString1370 {
    public String sortString(String s) {
        // Frequency array to count occurrences of each character
        int[] charCount = new int[26];
        for (char c : s.toCharArray()) {
            charCount[c - 'a']++;
        }

        StringBuilder result = new StringBuilder();
        int n = s.length();

        while (result.length() < n) {
            // Pick characters in increasing order
            for (int i = 0; i < 26; i++) {
                if (charCount[i] > 0) {
                    result.append((char) (i + 'a'));
                    charCount[i]--;
                }
            }

            // Pick characters in decreasing order
            for (int i = 25; i >= 0; i--) {
                if (charCount[i] > 0) {
                    result.append((char) (i + 'a'));
                    charCount[i]--;
                }
            }
        }

        return result.toString();
    }

    // Testing
    public static void main(String[] args) {
        IncreasingDecreasingString1370 solution = new IncreasingDecreasingString1370();
        String s = "aaaabbbbcccc";
        System.out.println("Java Test Result: " + solution.sortString(s));  // Output: "abccbaabccba"
    }
}
