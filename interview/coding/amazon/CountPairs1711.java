package amazon;

import java.util.HashMap;

public class CountPairs1711 {
    public int countPairs(int[] deliciousness) {
        int MOD = 1000000007;
        HashMap<Integer, Integer> countMap = new HashMap<>();
        int[] powerOfTwos = new int[22];
        for (int i = 0; i < 22; i++) {
            powerOfTwos[i] = 1 << i;  // 2^i
        }

        int count = 0;

        for (int d : deliciousness) {
            for (int target : powerOfTwos) {
                count = (count + countMap.getOrDefault(target - d, 0)) % MOD;
            }
            countMap.put(d, countMap.getOrDefault(d, 0) + 1);
        }

        return count;
    }

    // Testing the solution
    public static void main(String[] args) {
        CountPairs1711 solution = new CountPairs1711();

        // Test case
        int[] deliciousness = {1, 3, 5, 7, 9};
        System.out.println("Count of good meals: " + solution.countPairs(deliciousness));  // Expected output: 4
    }
}
