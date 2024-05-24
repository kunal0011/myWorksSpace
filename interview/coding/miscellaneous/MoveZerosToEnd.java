package miscellaneous;

import java.util.Arrays;

public class MoveZerosToEnd {
    public static void moveZerosToEnd(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return;
        }

        int left = 0;
        int right = 0;

        while (right < nums.length) {
            if (nums[right] != 0) {
                // Swap non-zero element with the element at the left pointer
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
            }
            right++;
        }
    }

    public static void main(String[] args) {
        int[] nums = {0, 1, 0, 3, 12};
        System.out.println("Original array: " + Arrays.toString(nums));
        moveZerosToEnd(nums);
        System.out.println("Array after moving zeros to the end: " + Arrays.toString(nums));
    }
}

