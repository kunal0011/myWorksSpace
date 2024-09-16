package amazon;

public class MinOperation1658 {
    public int minOperations(int[] nums, int x) {
        int target = 0;
        for (int num : nums) {
            target += num;
        }
        target -= x;

        if (target == 0) {
            return nums.length;  // The entire array sums to x
        }

        int n = nums.length;
        int currentSum = 0, maxLen = -1;
        int left = 0;

        for (int right = 0; right < n; right++) {
            currentSum += nums[right];

            // Shrink the window if the sum exceeds the target
            while (currentSum > target && left <= right) {
                currentSum -= nums[left];
                left++;
            }

            // Check if we found a subarray that sums to target
            if (currentSum == target) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
        }

        return maxLen != -1 ? n - maxLen : -1;
    }

    // Testing
    public static void main(String[] args) {
        MinOperation1658 solution = new MinOperation1658();
        int[] nums = {1, 1, 4, 2, 3};
        int x = 5;
        System.out.println("Java Test Result: " + solution.minOperations(nums, x));  // Output should be 2
    }
}

