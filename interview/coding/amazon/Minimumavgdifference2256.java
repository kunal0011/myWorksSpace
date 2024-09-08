package amazon;

public class Minimumavgdifference2256 {
    public int minimumAverageDifference(int[] nums) {
        int n = nums.length;
        long totalSum = 0;
        long prefixSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int resultIdx = -1;
        long minDiff = Long.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            // Update prefix sum
            prefixSum += nums[i];

            // Calculate the average of the first i + 1 elements
            long leftAvg = prefixSum / (i + 1);

            // Calculate the average of the last n - i - 1 elements
            long rightAvg = (i != n - 1) ? (totalSum - prefixSum) / (n - i - 1) : 0;

            // Calculate the absolute difference
            long diff = Math.abs(leftAvg - rightAvg);

            // Update the result if we found a smaller difference
            if (diff < minDiff) {
                minDiff = diff;
                resultIdx = i;
            }
        }

        return resultIdx;
    }

    public static void main(String[] args) {
        Minimumavgdifference2256 minavg = new Minimumavgdifference2256();
        System.out.println(minavg.minimumAverageDifference(new int[]{1, 2, 3, 45}))  ;
    }
}
