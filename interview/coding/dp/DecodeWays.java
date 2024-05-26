package dp;

public class DecodeWays {
    public static int countDecodings(String sequence) {
        if (sequence == null || sequence.length() == 0 || sequence.charAt(0) == '0') {
            return 0;
        }

        int n = sequence.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            char currentChar = sequence.charAt(i - 1);
            char previousChar = sequence.charAt(i - 2);

            // If the current character is not '0', add the number of ways to decode the sequence ending at the previous character
            if (currentChar != '0') {
                dp[i] += dp[i - 1];
            }

            // If the two-character number formed by the previous character and the current character is between 10 and 26, add the number of ways to decode the sequence ending at the character before the previous character
            if (previousChar == '1' || (previousChar == '2' && currentChar >= '0' && currentChar <= '6')) {
                dp[i] += dp[i - 2];
            }
        }

        return dp[n];
    }

    public static void main(String[] args) {
        String sequence = "123";
        System.out.println(countDecodings(sequence));  // Output: 3
    }
}

