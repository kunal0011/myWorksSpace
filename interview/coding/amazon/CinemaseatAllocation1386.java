package amazon;

import java.util.*;

public class CinemaseatAllocation1386 {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        Map<Integer, Set<Integer>> reserved = new HashMap<>();

        // Mark reserved seats for each row
        for (int[] seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];
            reserved.putIfAbsent(row, new HashSet<>());
            reserved.get(row).add(col);
        }

        int totalFamilies = 2 * n;  // Initially assume all rows can fit 2 families

        for (int row : reserved.keySet()) {
            Set<Integer> reservedInRow = reserved.get(row);
            boolean canPlaceLeft = !(reservedInRow.contains(2) || reservedInRow.contains(3) || reservedInRow.contains(4) || reservedInRow.contains(5));
            boolean canPlaceRight = !(reservedInRow.contains(6) || reservedInRow.contains(7) || reservedInRow.contains(8) || reservedInRow.contains(9));
            boolean canPlaceMiddle = !(reservedInRow.contains(4) || reservedInRow.contains(5) || reservedInRow.contains(6) || reservedInRow.contains(7));

            int familiesInThisRow = 0;

            if (canPlaceLeft) {
                familiesInThisRow += 1;
            }
            if (canPlaceRight) {
                familiesInThisRow += 1;
            }
            if (familiesInThisRow == 0 && canPlaceMiddle) {
                familiesInThisRow += 1;
            }

            totalFamilies -= (2 - familiesInThisRow);
        }

        return totalFamilies;
    }

    // Test cases
    public static void main(String[] args) {
        CinemaseatAllocation1386 sol = new CinemaseatAllocation1386();

        // Test case 1
        int n1 = 3;
        int[][] reservedSeats1 = {{1, 2}, {1, 3}, {1, 8}, {2, 6}, {3, 1}, {3, 10}};
        assert sol.maxNumberOfFamilies(n1, reservedSeats1) == 4 : "Test case 1 failed";

        // Test case 2
        int n2 = 2;
        int[][] reservedSeats2 = {{2, 1}, {1, 8}, {2, 6}};
        assert sol.maxNumberOfFamilies(n2, reservedSeats2) == 2 : "Test case 2 failed";

        // Test case 3
        int n3 = 4;
        int[][] reservedSeats3 = {{4, 3}, {4, 4}, {4, 7}, {4, 8}, {4, 9}, {1, 10}, {2, 2}};
        assert sol.maxNumberOfFamilies(n3, reservedSeats3) == 4 : "Test case 3 failed";

        System.out.println("All test cases passed!");
    }
}
