package amazon;

public class SumOfbeauty2012 {
    public int sumOfBeauties(int[] nums) {
        int n = nums.length;
        int[] leftMax = new int[n];
        int[] rightMin = new int[n];

        // Fill the leftMax array
        leftMax[0] = nums[0];
        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], nums[i]);
        }

        // Fill the rightMin array
        rightMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            rightMin[i] = Math.min(rightMin[i + 1], nums[i]);
        }

        int sumOfBeauty = 0;

        // Calculate the beauty for each index
        for (int i = 1; i < n - 1; i++) {
             if (leftMax[i - 1] < nums[i] && nums[i] < rightMin[i + 1]) {
                sumOfBeauty += 2;
            }else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) {
                 sumOfBeauty += 2;
             }
        }

        return sumOfBeauty;
    }
}
