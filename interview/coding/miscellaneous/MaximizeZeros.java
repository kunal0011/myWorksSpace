package miscellaneous;

public class MaximizeZeros {

    public static int maximizeZeros(int[] arr) {
        int n = arr.length;

        // If the array has all zeros, flipping any part will not increase zeros, just return count of all zeros
        int totalZeros = 0;
        for (int value : arr) {
            if (value == 0) {
                totalZeros++;
            }
        }
        if (totalZeros == n) {
            return totalZeros;
        }

        // Step 1: Transform the array
        int[] transformedArr = new int[n];
        for (int i = 0; i < n; i++) {
            transformedArr[i] = (arr[i] == 0) ? 1 : -1;
        }

        // Step 2: Find the maximum sum subarray in the transformed array using Kadane's algorithm
        int maxEndingHere = 0;
        int maxSoFar = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            maxEndingHere += transformedArr[i];
            if (maxEndingHere > maxSoFar) {
                maxSoFar = maxEndingHere;
            }
            if (maxEndingHere < 0) {
                maxEndingHere = 0;
            }
        }

        // The maximum increase in number of 0s we can get by flipping a subarray is maxSoFar
        int maxIncreaseInZeros = maxSoFar;

        // Result is the original number of 0s plus the maximum increase found
        return totalZeros + maxIncreaseInZeros;
    }

    public static void main(String[] args) {
        int[] arr = {1, 0, 0, 1, 0, 1, 0, 1, 1};
        System.out.println("Maximum number of 0s after flipping a subarray: " + maximizeZeros(arr));
    }
}
