package amazon;

public class PatchinArray330 {
    public int minPatches(int[] nums, int n) {
        int patches = 0;
        int i = 0;
        long currentRange = 1;  // Use long to avoid overflow

        while (currentRange <= n) {
            // If nums[i] can extend the range, use it
            if (i < nums.length && nums[i] <= currentRange) {
                currentRange += nums[i];
                i++;
            } else {
                // Add a patch equal to currentRange
                currentRange += currentRange;
                patches++;
            }
        }

        return patches;
    }
}

