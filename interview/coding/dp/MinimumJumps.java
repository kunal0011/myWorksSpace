package dp;

public class MinimumJumps {
    public static int minJumps(int[] arr) {
        int n = arr.length;
        if (n <= 1) {
            return 0;
        }

        int[] dp = new int[n];
        dp[0] = 0;

        for (int i = 1; i < n; i++) {
            dp[i] = Integer.MAX_VALUE;
            for (int j = 0; j < i; j++) {
                if (j + arr[j] >= i && dp[j] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
        }

        return dp[n - 1];
    }

    public static void main(String[] args) {
        int[] arr = {2, 3, 1, 1, 2, 4, 2, 0, 1, 1};
        System.out.println("Minimum number of jumps: " + minJumps(arr)); // Output: 4
    }
}
