package miscellaneous;

import java.util.Arrays;

public class ClosestSumToZero {

    // Function to find the sum of two elements whose sum is closest to zero
    public static int[] closestSumToZero(int[] arr) {
        // Sort the array
        Arrays.sort(arr);

        int left = 0;
        int right = arr.length - 1;
        int minSum = Integer.MAX_VALUE;
        int[] closestPair = new int[2];

        // Two pointers approach
        while (left < right) {
            int sum = arr[left] + arr[right];
            // Update closest sum found so far
            if (Math.abs(sum) < Math.abs(minSum)) {
                minSum = sum;
                closestPair[0] = arr[left];
                closestPair[1] = arr[right];
            }
            // Move pointers based on the sum
            if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }

        return closestPair;
    }

    public static void main(String[] args) {
        int[] arr = {-4, -2, 1, 5, 6, 7};
        int[] closestPair = closestSumToZero(arr);
        System.out.println("Closest pair with sum closest to zero: " + closestPair[0] + ", " + closestPair[1]);
    }
}
