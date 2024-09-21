package amazon;

public class Numberofderangement634 {
    public int findDerangement(int n) {
        final int MOD = 1000000007;

        if (n == 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }

        long[] dp = new long[n + 1];
        dp[0] = 1;  // Base case: D(0) = 1 (by convention)
        dp[1] = 0;  // Base case: D(1) = 0

        // Fill the dp array using the recurrence relation
        for (int i = 2; i <= n; i++) {
            dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD;
        }

        return (int) dp[n];
    }

    // Test cases
    public static void main(String[] args) {
        Numberofderangement634 sol = new Numberofderangement634();

        // Test case 1
        int n1 = 3;
        System.out.println(sol.findDerangement(n1));  // Output: 2

        // Test case 2
        int n2 = 2;
        System.out.println(sol.findDerangement(n2));  // Output: 1

        // Test case 3
        int n3 = 4;
        System.out.println(sol.findDerangement(n3));  // Output: 9
    }
}

