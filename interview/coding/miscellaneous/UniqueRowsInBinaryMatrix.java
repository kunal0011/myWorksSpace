package miscellaneous;

import java.util.HashSet;
import java.util.Set;

public class UniqueRowsInBinaryMatrix {
    public static void printUniqueRows(int[][] matrix) {
        Set<String> uniqueRows = new HashSet<>();

        for (int[] row : matrix) {
            StringBuilder sb = new StringBuilder();
            for (int num : row) {
                sb.append(num);
            }
            String rowString = sb.toString();

            if (!uniqueRows.contains(rowString)) {
                System.out.println(rowString);
                uniqueRows.add(rowString);
            }
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {1, 0, 0, 1},
                {0, 1, 0, 0},
                {1, 0, 0, 1},
                {0, 1, 1, 0}
        };

        System.out.println("Unique rows in the binary matrix:");
        printUniqueRows(matrix);
    }
}

