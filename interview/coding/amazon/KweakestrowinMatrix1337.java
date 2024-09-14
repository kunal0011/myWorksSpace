package amazon;

import java.util.*;

public class KweakestrowinMatrix1337 {
    public int[] kWeakestRows(int[][] mat, int k) {
        // Create a list of (number_of_ones, row_index)
        List<int[]> rowStrengths = new ArrayList<>();
        for (int i = 0; i < mat.length; i++) {
            int countOnes = 0;
            for (int num : mat[i]) {
                if (num == 1) countOnes++;
            }
            rowStrengths.add(new int[]{countOnes, i});
        }

        // Sort the list by number_of_ones and then by row_index
        rowStrengths.sort((a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });

        // Extract the indices of the k weakest rows
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = rowStrengths.get(i)[1];
        }
        return result;
    }
}

