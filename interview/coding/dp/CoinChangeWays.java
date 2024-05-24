package dp;

public class CoinChangeWays {
    public static int numberOfWays(int[] coins, int amount) {
        // Initialize the DP table with 0 for all amounts
        int[] dp = new int[amount + 1];

        // Base case: There is one way to make amount 0 (using no coins)
        dp[0] = 1;

        // Iterate through each coin
        for (int coin : coins) {
            // Update the DP table for all amounts from the coin value to the target amount
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }

        // Return the number of ways to make the target amount
        return dp[amount];
    }

    public static void main(String[] args) {
        int[] coins = {1, 5, 10, 25, 50};
        int amount = 63;
        int result = numberOfWays(coins, amount);
        System.out.println("Number of ways to make change: " + result);
    }
}

