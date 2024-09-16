package amazon;

public class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] result = new int[2 * n];
        int index = 0;

        // Interleave elements from both halves
        for (int i = 0; i < n; i++) {
            result[index++] = nums[i];
            result[index++] = nums[i + n];
        }

        return result;
    }

    // Testing
    public static void main(String[] args) {
        Rearrangwwords1451 solution = new Rearrangwwords1451();
        int[] nums = {2, 5, 1, 3, 4, 7};
        int n = 3;
        int[] result = solution.shuffle(nums, n);
        System.out.print("Java Test Result: ");
        for (int num : result) {
            System.out.print(num + " ");
        }
        // Output should be [2, 3, 5, 4, 1, 7]
    }
}

