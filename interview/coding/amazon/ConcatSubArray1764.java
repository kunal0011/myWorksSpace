package amazon;

public class ConcatSubArray1764 {
    public boolean canChoose(int[][] groups, int[] nums) {
        int n = nums.length;
        int idx = 0;  // index in nums

        // Loop over each group in groups
        for (int[] group : groups) {
            boolean found = false;

            // Try to find the group as a subarray in nums starting from index idx
            while (idx + group.length <= n) {
                boolean match = true;

                // Check if group matches nums starting from idx
                for (int i = 0; i < group.length; i++) {
                    if (nums[idx + i] != group[i]) {
                        match = false;
                        break;
                    }
                }

                // If match is found, move idx forward by the length of the group
                if (match) {
                    found = true;
                    idx += group.length;
                    break;
                }

                // Otherwise, move to the next index in nums
                idx++;
            }

            // If the group is not found as a subarray in nums, return false
            if (!found) {
                return false;
            }
        }

        return true;
    }
}
