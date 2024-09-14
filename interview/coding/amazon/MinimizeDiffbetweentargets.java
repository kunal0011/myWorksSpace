package amazon;

import java.util.HashSet;
import java.util.Set;

public class MinimizeDiffbetweentargets {
    public int minimizeTheDifference(int[][] mat, int target) {
        // We use a set to store possible sums for each row
        Set<Integer> possibleSums = new HashSet<>();
        possibleSums.add(0);

        for (int[] row : mat) {
            Set<Integer> newSums = new HashSet<>();
            for (int num : row) {
                for (int sum : possibleSums) {
                    newSums.add(sum + num);
                }
            }
            possibleSums = newSums; // Update the possible sums with new calculated sums
        }

        // Find the minimum absolute difference
        int minDiff = Integer.MAX_VALUE;
        for (int sum : possibleSums) {
            minDiff = Math.min(minDiff, Math.abs(sum - target));
        }

        return minDiff;
    }
}
