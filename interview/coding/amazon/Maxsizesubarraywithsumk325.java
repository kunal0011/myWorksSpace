package amazon;

import java.util.HashMap;

public class Maxsizesubarraywithsumk325 {
    public int maxSubArrayLen(int[] nums, int k) {
        HashMap<Integer, Integer> prefixSum = new HashMap<>();
        prefixSum.put(0, -1);
        int currentSum = 0;
        int maxLen = 0;

        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            if (prefixSum.containsKey(currentSum - k)) {
                maxLen = Math.max(maxLen, i - prefixSum.get(currentSum - k));
            }
            prefixSum.putIfAbsent(currentSum, i);
        }

        return maxLen;
    }
}
