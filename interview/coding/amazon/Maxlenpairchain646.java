package amazon;

import java.util.Arrays;

public class Maxlenpairchain646 {
    public int findLongestChain(int[][] pairs) {
        // Sort the pairs by the second element
        Arrays.sort(pairs, (a, b) -> Integer.compare(a[1], b[1]));

        int currEnd = Integer.MIN_VALUE;
        int count = 0;

        // Iterate through the pairs
        for (int[] pair : pairs) {
            if (pair[0] > currEnd) {
                currEnd = pair[1];
                count++;
            }
        }

        return count;
    }

    // Test cases
    public static void main(String[] args) {
        Maxlenpairchain646 sol = new Maxlenpairchain646();

        // Test case 1
        int[][] pairs1 = {{1, 2}, {2, 3}, {3, 4}};
        System.out.println(sol.findLongestChain(pairs1));  // Output: 2

        // Test case 2
        int[][] pairs2 = {{1, 2}, {7, 8}, {4, 5}};
        System.out.println(sol.findLongestChain(pairs2));  // Output: 3
    }
}
