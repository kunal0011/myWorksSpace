package amazon;

 import java.util.Arrays;

public class Campusbikeii1066 {
    private int[][] workers;
    private int[][] bikes;
    private int[][] memo;

    public int assignBikes(int[][] workers, int[][] bikes) {
        this.workers = workers;
        this.bikes = bikes;
        int n = workers.length;
        int m = bikes.length;

        // Initialize memoization table with -1 (uncomputed states)
        memo = new int[n][1 << m];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        // Start from worker 0 and no bikes used
        return dp(0, 0);
    }

    private int dp(int worker, int usedBikes) {
        // Base case: All workers are assigned
        if (worker == workers.length) {
            return 0;
        }

        // If this state has been computed before, return the result
        if (memo[worker][usedBikes] != -1) {
            return memo[worker][usedBikes];
        }

        // Try all available bikes and calculate the minimum cost
        int minCost = Integer.MAX_VALUE;
        for (int bike = 0; bike < bikes.length; bike++) {
            if ((usedBikes & (1 << bike)) == 0) {  // If this bike hasn't been used
                int dist = manhattan(workers[worker], bikes[bike]);
                minCost = Math.min(minCost, dist + dp(worker + 1, usedBikes | (1 << bike)));
            }
        }

        // Memoize the result and return it
        memo[worker][usedBikes] = minCost;
        return minCost;
    }

    // Helper function to calculate Manhattan distance
    private int manhattan(int[] worker, int[] bike) {
        return Math.abs(worker[0] - bike[0]) + Math.abs(worker[1] - bike[1]);
    }

    // Testing
    public static void main(String[] args) {
        Campusbikeii1066 solution = new Campusbikeii1066();
        int[][] workers = {{0, 0}, {2, 1}};
        int[][] bikes = {{1, 2}, {3, 3}};
        System.out.println("Java Test Result: " + solution.assignBikes(workers, bikes));  // Output: 6
    }
}

