package amazon;

public class FindJudge997 {
public int findJudge(int n, int[][] trust) {
        if (n == 1 && trust.length == 0) {
        return 1;
        }

        int[] trustScores = new int[n + 1];

        // Process the trust array
        for (int[] t : trust) {
        trustScores[t[0]]--;  // t[0] trusts someone
        trustScores[t[1]]++;  // t[1] is trusted
        }

        // Check if there's a person with score n-1 (the judge)
        for (int i = 1; i <= n; i++) {
        if (trustScores[i] == n - 1) {
        return i;
        }
        }

        return -1;
        }

// Testing
public static void main(String[] args) {
        FindJudge997 solution = new FindJudge997();
        int n = 3;
        int[][] trust = {{1, 3}, {2, 3}};
        System.out.println("Java Test Result: " + solution.findJudge(n, trust));  // Output: 3
        }
        }
