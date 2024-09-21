package amazon;

public class MinimumdeleteOperation583 {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();

        // dp[i][j] will hold the length of LCS of word1[0:i] and word2[0:j]
        int[][] dp = new int[m + 1][n + 1];

        // Build the dp array
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        // The number of deletions required is the sum of the lengths of the strings
        // minus twice the length of their LCS
        int lcsLength = dp[m][n];
        return (m - lcsLength) + (n - lcsLength);
    }

    // Test case
    public static void main(String[] args) {
        MinimumdeleteOperation583 sol = new MinimumdeleteOperation583();

        // Test case 1
        String word1 = "sea";
        String word2 = "eat";
        System.out.println(sol.minDistance(word1, word2));  // Expected output: 2

        // Test case 2
//        String word1 = "leetcode";
//        String word2 = "etco";
//        System.out.println(sol.minDistance(word1, word2));  // Expected output: 4
    }
}
