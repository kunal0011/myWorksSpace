package amazon;

import java.util.*;

public class OptimalAccountBalancing465 {
    public int minTransfers(int[][] transactions) {
        Map<Integer, Integer> balance = new HashMap<>();

        // Step 1: Calculate net balances
        for (int[] t : transactions) {
            int giver = t[0], receiver = t[1], amount = t[2];
            balance.put(giver, balance.getOrDefault(giver, 0) - amount);
            balance.put(receiver, balance.getOrDefault(receiver, 0) + amount);
        }

        // Step 2: Remove zero balances (people who have no net debt)
        List<Integer> debt = new ArrayList<>();
        for (int b : balance.values()) {
            if (b != 0) {
                debt.add(b);
            }
        }

        // Backtracking function to minimize transactions
        return settle(debt, 0);
    }

    private int settle(List<Integer> debt, int start) {
        // Skip already settled debts
        while (start < debt.size() && debt.get(start) == 0) {
            start++;
        }
        if (start == debt.size()) {
            return 0;
        }

        int minTransactions = Integer.MAX_VALUE;
        for (int i = start + 1; i < debt.size(); i++) {
            if (debt.get(i) * debt.get(start) < 0) { // opposite signs, can settle
                // Settle debt[start] with debt[i]
                debt.set(i, debt.get(i) + debt.get(start));
                minTransactions = Math.min(minTransactions, 1 + settle(debt, start + 1));
                // Backtrack
                debt.set(i, debt.get(i) - debt.get(start));
            }
        }

        return minTransactions;
    }

    // Test cases
    public static void main(String[] args) {
        OptimalAccountBalancing465 sol = new OptimalAccountBalancing465();

        // Test case 1
        int[][] transactions1 = {{0, 1, 10}, {2, 0, 5}};
        System.out.println(sol.minTransfers(transactions1));  // Expected output: 2

        // Test case 2
        int[][] transactions2 = {{0, 1, 10}, {1, 2, 5}, {2, 0, 5}};
        System.out.println(sol.minTransfers(transactions2));  // Expected output: 1
    }
}

