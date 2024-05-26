package dp;

public class EditDistance {
    public static int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();

        // dp array to store the edit distances
        int[][] dp = new int[m + 1][n + 1];

        // Initialize base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;  // Deleting all characters from word1
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;  // Inserting all characters of word2
        }

        // Fill the dp array
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j] + 1,   // Deletion
                            Math.min(dp[i][j - 1] + 1,   // Insertion
                                    dp[i - 1][j - 1] + 1));  // Substitution
                }
            }
        }

        return dp[m][n];
    }

    public static void main(String[] args) {
        String word1 = "kitten";
        String word2 = "sitting";
        System.out.println(minDistance(word1, word2));  // Output: 3
    }
}
