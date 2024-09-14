package amazon;

import java.util.*;

public class NumberOfEquivalentDomino1128 {
    public int numEquivDominoPairs(int[][] dominoes) {
        Map<String, Integer> count = new HashMap<>();

        // Normalize and count each domino
        for (int[] domino : dominoes) {
            int a = domino[0];
            int b = domino[1];
            String key = a < b ? a + "," + b : b + "," + a;
            count.put(key, count.getOrDefault(key, 0) + 1);
        }

        // Calculate number of equivalent pairs
        int result = 0;
        for (int freq : count.values()) {
            if (freq > 1) {
                result += freq * (freq - 1) / 2;
            }
        }

        return result;
    }
}

