package amazon;

import java.util.*;

public class Pyramidtransitionmatrix756 {
    // Memoization map to store results of subproblems
    private Map<String, Boolean> memo = new HashMap<>();
    // Map to store all possible transitions for a pair of blocks
    private Map<String, List<Character>> transitions = new HashMap<>();

    public boolean pyramidTransition(String bottom, List<String> allowed) {
        // Populate the transitions map
        for (String triple : allowed) {
            String base = triple.substring(0, 2);  // Get the first two characters
            char top = triple.charAt(2);  // Get the top block

            transitions.computeIfAbsent(base, k -> new ArrayList<>()).add(top);
        }

        // Start the recursive process from the bottom row
        return canBuild(bottom);
    }

    // Recursive function to determine if we can build the pyramid
    private boolean canBuild(String row) {
        // Base case: if we have reached the top with a single block
        if (row.length() == 1) return true;

        // Check if this row's result is already computed
        if (memo.containsKey(row)) return memo.get(row);

        // Try to build all possible next rows and check if any can lead to a valid pyramid
        for (String nextRow : buildNextRow(row, 0, new StringBuilder())) {
            if (canBuild(nextRow)) {
                memo.put(row, true);
                return true;
            }
        }

        // If no valid pyramid can be built, store the result as false
        memo.put(row, false);
        return false;
    }

    // Helper function to build all possible next rows
    private List<String> buildNextRow(String row, int index, StringBuilder current) {
        List<String> nextRows = new ArrayList<>();

        // If we have processed the whole row, add the built row to the results
        if (index == row.length() - 1) {
            nextRows.add(current.toString());
        } else {
            // Get the pair of adjacent blocks in the current row
            String pair = row.substring(index, index + 2);

            // If there's a valid transition for the pair, try to form the next row
            if (transitions.containsKey(pair)) {
                for (char block : transitions.get(pair)) {
                    current.append(block);  // Add the new block to the next row
                    nextRows.addAll(buildNextRow(row, index + 1, current));  // Recursively build the row
                    current.deleteCharAt(current.length() - 1);  // Backtrack to try other options
                }
            }
        }

        return nextRows;
    }

    // Test cases
    public static void main(String[] args) {
        Pyramidtransitionmatrix756 sol = new Pyramidtransitionmatrix756();

        // Test case 1
        String bottom1 = "BCD";
        List<String> allowed1 = Arrays.asList("BCG", "CDE", "GEA", "FFF");
        System.out.println(sol.pyramidTransition(bottom1, allowed1));  // Expected output: true

        // Test case 2
        String bottom2 = "AABA";
        List<String> allowed2 = Arrays.asList("AAA", "AAB", "ABA", "ABB", "BAC");
        System.out.println(sol.pyramidTransition(bottom2, allowed2));  // Expected output: false
    }
}
