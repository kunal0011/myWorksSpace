package amazon;

import java.util.*;

public class Binarytreewithfactor823 {
    public int numFactoredBinaryTrees(int[] arr) {
        int MOD = 1_000_000_007;
        Arrays.sort(arr);
        Map<Integer, Long> dp = new HashMap<>();

        for (int num : arr) {
            dp.put(num, 1L);  // Every number can form at least one tree with itself as the root.
        }

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] % arr[j] == 0) {  // arr[i] = arr[j] * another number
                    int right = arr[i] / arr[j];
                    if (dp.containsKey(right)) {
                        dp.put(arr[i], (dp.get(arr[i]) + dp.get(arr[j]) * dp.get(right)) % MOD);
                    }
                }
            }
        }

        long result = 0;
        for (long count : dp.values()) {
            result = (result + count) % MOD;
        }
        return (int) result;
    }

    // Test cases
    public static void main(String[] args) {
        Binarytreewithfactor823 sol = new Binarytreewithfactor823();

        // Test case 1
        int[] arr1 = {2, 4};
        System.out.println(sol.numFactoredBinaryTrees(arr1));  // Expected output: 3

        // Test case 2
        int[] arr2 = {2, 4, 5, 10};
        System.out.println(sol.numFactoredBinaryTrees(arr2));  // Expected output: 7
    }
}

