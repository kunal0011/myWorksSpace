package dp;

public class ZeroOneKnapsackOptimized {

    // Function to solve the 0/1 knapsack problem with space optimization
    public static int knapsack(int W, int[] w, int[] v) {
        int n = w.length;
        int[] dp = new int[W + 1];

        // Iterate over each item
        for (int i = 0; i < n; i++) {
            // Iterate over capacities from W to w[i] (backward)
            for (int j = W; j >= w[i]; j--) {
                dp[j] = Math.max(dp[j], v[i] + dp[j - w[i]]);
            }
        }

        return dp[W];
    }

    public static void main(String[] args) {
        int W = 50; // Maximum capacity of the knapsack
        int[] w = {10, 20, 30}; // Weights of the items
        int[] v = {60, 100, 120}; // Values of the items

        int maxValue = knapsack(W, w, v);
        System.out.println("Maximum value: " + maxValue); // Output: 220
    }
}
