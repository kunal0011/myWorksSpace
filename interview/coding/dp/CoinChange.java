package dp;

import java.util.Arrays;

public class CoinChange {
    public static int minCoins(int[] coins, int amount) {
        // Initialize the DP table with a large value (infinity)
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);

        // Base case: 0 coins are needed to make 0 amount
        dp[0] = 0;

        // Iterate through all amounts from 1 to the target amount
        for (int i = 1; i <= amount; i++) {
            // Check each coin denomination
            for (int coin : coins) {
                if (coin <= i) {
                    // Update the DP table if a new minimum is found
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        // If dp[amount] is still a large value, it means it's not possible to form the amount
        return dp[amount] > amount ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        int[] coins = {1, 5, 10, 25, 50};
        int amount = 63;
        int result = minCoins(coins, amount);
        System.out.println("Minimum number of coins needed: " + result);
    }
}
