package dp;

public class UnboundedKnapsack {
    // Function to solve the unbounded knapsack problem
    public static int unboundedKnapsack(int W, int[] w, int[] v) {
        int n = w.length;
        int[] dp = new int[W + 1];

        // Iterate over all possible capacities
        for (int j = 0; j <= W; j++) {
            // Iterate over all items
            for (int i = 0; i < n; i++) {
                if (w[i] <= j) {
                    dp[j] = Math.max(dp[j], dp[j - w[i]] + v[i]);
                }
            }
        }

        return dp[W];
    }

    public static void main(String[] args) {
        int W = 100; // Maximum capacity of the knapsack
        int[] w = {1, 50}; // Weights of the items
        int[] v = {1, 30}; // Values of the items

        int maxValue = unboundedKnapsack(W, w, v);
        System.out.println("Maximum value: " + maxValue);
    }
}
