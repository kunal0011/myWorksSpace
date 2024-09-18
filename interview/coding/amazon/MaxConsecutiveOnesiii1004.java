package amazon;

public class MaxConsecutiveOnesiii1004 {
    public int longestOnes(int[] nums, int K) {
        int left = 0, maxLength = 0, zeroCount = 0;

        for (int right = 0; right < nums.length; right++) {
            // If we encounter a 0, increase the zero count
            if (nums[right] == 0) {
                zeroCount++;
            }

            // If zero count exceeds K, move the left pointer to reduce zeros
            while (zeroCount > K) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }

            // Calculate the length of the current window
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    // Testing
    public static void main(String[] args) {
        MaxConsecutiveOnesiii1004 solution = new MaxConsecutiveOnesiii1004();
        int[] nums = {1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1};
        int K = 2;
        System.out.println("Java Test Result: " + solution.longestOnes(nums, K));  // Output: 6
    }
}
