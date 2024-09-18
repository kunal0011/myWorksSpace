package amazon;

public class DecodeStringatindezx880 {
    public String decodeAtIndex(String S, int K) {
        long size = 0;

        // First pass: find the length of the fully decoded string
        for (char c : S.toCharArray()) {
            if (Character.isDigit(c)) {
                size *= c - '0';  // Multiply the size when encountering a digit
            } else {
                size++;  // Increase size for each letter
            }
        }

        // Second pass: work backwards to find the K-th character
        for (int i = S.length() - 1; i >= 0; i--) {
            char c = S.charAt(i);
            K %= size;  // Reduce K to be within the current size

            if (K == 0 && Character.isLetter(c)) {
                return String.valueOf(c);
            }

            if (Character.isDigit(c)) {
                size /= c - '0';  // Divide size by the digit value
            } else {
                size--;  // Decrease size for each letter
            }
        }
        return "";
    }

    // Test cases
    public static void main(String[] args) {
        DecodeStringatindezx880 sol = new DecodeStringatindezx880();

        // Test case 1
        String S1 = "leet2code3";
        int K1 = 10;
        System.out.println(sol.decodeAtIndex(S1, K1));  // Expected output: "o"

        // Test case 2
        String S2 = "ha22";
        int K2 = 5;
        System.out.println(sol.decodeAtIndex(S2, K2));  // Expected output: "h"

    }
}