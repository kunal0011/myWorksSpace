package amazon;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class ThreeSumWithMultiplicity923 {
    public int threeSumMulti(int[] A, int target) {
        final int MOD = 1000000007;
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : A) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        int[] keys = count.keySet().stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(keys);
        long ans = 0;

        // Iterate over all combinations of 3 distinct keys
        for (int i = 0; i < keys.length; i++) {
            int x = keys[i];
            for (int j = i; j < keys.length; j++) {
                int y = keys[j];
                for (int k = j; k < keys.length; k++) {
                    int z = keys[k];

                    if (x + y + z == target) {
                        if (x == y && y == z) {
                            ans += (long) count.get(x) * (count.get(x) - 1) * (count.get(x) - 2) / 6;
                        } else if (x == y) {
                            ans += (long) count.get(x) * (count.get(x) - 1) / 2 * count.get(z);
                        } else if (y == z) {
                            ans += (long) count.get(y) * (count.get(y) - 1) / 2 * count.get(x);
                        } else {
                            ans += (long) count.get(x) * count.get(y) * count.get(z);
                        }
                    }
                }
            }
        }

        return (int) (ans % MOD);
    }

    // Test cases
    public static void main(String[] args) {
        ThreeSumWithMultiplicity923 sol = new ThreeSumWithMultiplicity923();

        // Test case 1
        int[] A1 = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5};
        int target1 = 8;
        System.out.println(sol.threeSumMulti(A1, target1));  // Expected output: 20

        // Test case 2
        int[] A2 = {1, 1, 1, 1, 1};
        int target2 = 3;
        System.out.println(sol.threeSumMulti(A2, target2));  // Expected output: 10
    }
}

