package searching_sorting;

import java.util.Arrays;

public class Sort012 {
    public static void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;

        // Traverse the array
        while (mid <= high) {
            switch (nums[mid]) {
                case 0:
                    // Swap the elements at mid and low pointers and move both pointers forward
                    swap(nums, low, mid);
                    low++;
                    mid++;
                    break;
                case 1:
                    // If the element is 1, just move the mid pointer forward
                    mid++;
                    break;
                case 2:
                    // Swap the elements at mid and high pointers and move the high pointer backward
                    swap(nums, mid, high);
                    high--;
                    break;
            }
        }
    }

    // Helper function to swap elements in the array
    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    // Function to print the array
    public static void printArray(int[] nums) {
        System.out.println(Arrays.toString(nums));
    }

    public static void main(String[] args) {
        int[] nums = {0, 1, 2, 1, 0, 2, 1, 2, 0};

        System.out.println("Original array:");
        printArray(nums);

        sortColors(nums);

        System.out.println("Sorted array:");
        printArray(nums);
    }
}
