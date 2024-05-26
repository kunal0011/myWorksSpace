package dp;

public class SpecialKeyboard {

    public static int maxA(int N) {
        if (N <= 0) return 0;
        if (N <= 6) return N;  // For N from 1 to 6, the best strategy is to just press 'A' key.

        // dp array to store the maximum number of 'A's with i key presses
        int[] dp = new int[N + 1];

        // Initialize base cases
        for (int i = 1; i <= 6; i++) {
            dp[i] = i;
        }

        // Fill the dp array
        for (int i = 7; i <= N; i++) {
            dp[i] = dp[i - 1] + 1; // Assume the best strategy is to just press 'A' key
            // Check the effect of using (ctrl-A), (ctrl-C), and multiple (ctrl-V)
            for (int j = i - 3; j >= 1; j--) {
                dp[i] = Math.max(dp[i], dp[j] * (i - j - 1));
            }
        }

        return dp[N];
    }

    public static void main(String[] args) {
        int N = 11;
        System.out.println("Maximum number of 'A's with " + N + " key presses: " + maxA(N));
    }
}
