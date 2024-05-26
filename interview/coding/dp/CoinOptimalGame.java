package dp;

public class CoinOptimalGame {
    public static int maxCoinValue(int[] coins) {
        int n = coins.length;
        int[][] dp = new int[n][n];

        // Base cases: when there's only one coin, the value is the coin itself.
        for (int i = 0; i < n; i++) {
            dp[i][i] = coins[i];
        }

        // Fill the table using the recurrence relation
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i <= n - length; i++) {
                int j = i + length - 1;
                int x = (i + 2 <= j) ? dp[i + 2][j] : 0;
                int y = (i + 1 <= j - 1) ? dp[i + 1][j - 1] : 0;
                int z = (i <= j - 2) ? dp[i][j - 2] : 0;

                dp[i][j] = Math.max(coins[i] + Math.min(x, y),
                        coins[j] + Math.min(y, z));
            }
        }

        return dp[0][n - 1];
    }

    public static void main(String[] args) {
        int[] coins = {8, 15, 3, 7};
        System.out.println("Maximum value player 1 can collect: " + maxCoinValue(coins)); // Output: 22
    }
}
