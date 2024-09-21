package amazon;

import java.util.List;

public class RangeAdditionii598 {
    public int maxCount(int m, int n, List<List<Integer>> operations) {
        if (operations.isEmpty()) {
            return m * n;
        }

        int minA = m;
        int minB = n;

        for (List<Integer> op : operations) {
            minA = Math.min(minA, op.get(0));
            minB = Math.min(minB, op.get(1));
        }

        return minA * minB;
    }

    // Test cases
    public static void main(String[] args) {
        RangeAdditionii598 sol = new RangeAdditionii598();

        // Test case 1
//        int m1 = 3, n1 = 3;
//        List<List<Integer>> operations1 = List.of(List.of(2, 2), List.of(3, 3));
//        System.out.println(sol.maxCount(m1, n1, operations1));  // Output: 4
//
//        // Test case 2
//        int m2 = 3, n2 = 3;
//        List<List<Integer>> operations2 = List.of(List.of(2, 2), List.of(3, 3), List.of(1, 1));
//        System.out.println(sol.maxCount(m2, n2, operations2));  // Output: 1
    }
}

