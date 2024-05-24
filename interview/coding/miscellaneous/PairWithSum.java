package miscellaneous;

import java.util.Arrays;

public class PairWithSum {
    public static boolean hasPairWithSum(int[] arr, int x) {
        // Sort the array
        Arrays.sort(arr);

        // Initialize two pointers
        int left = 0;
        int right = arr.length - 1;

        // Iterate while the left pointer is less than the right pointer
        while (left < right) {
            int sum = arr[left] + arr[right];

            // Check if the sum of elements at left and right pointers equals x
            if (sum == x) {
                return true;
            }

            // Move the left pointer to the right if the sum is less than x
            if (sum < x) {
                left++;
            }
            // Move the right pointer to the left if the sum is greater than x
            else {
                right--;
            }
        }

        // If no pair is found, return false
        return false;
    }

    public static void main(String[] args) {
        int[] arr = {10, 15, 3, 7};
        int x = 17;
        boolean result = hasPairWithSum(arr, x);
        System.out.println("Has pair with sum " + x + ": " + result);
    }
}
