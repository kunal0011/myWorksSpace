package miscellaneous;

public class MaxSumOfLengthsOfSubarraysWithK {

    // Maximum sum of lengths of non-overlapping subarrays with k as the max element.
    public static int maxSumOfLengthsWithK(int[] arr, int k) {
        int maxSumLengths = 0;
        int currentLength = 0;
        boolean containsK = false;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > k) {
                // End the current subarray
                if (containsK) {
                    maxSumLengths += currentLength;
                }
                currentLength = 0;
                containsK = false;
            } else {
                // Continue the current subarray
                currentLength++;
                if (arr[i] == k) {
                    containsK = true;
                }
            }
        }

        // Add the last subarray if it contains k
        if (containsK) {
            maxSumLengths += currentLength;
        }

        return maxSumLengths;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 2, 5, 2, 1, 2, 3, 4};
        int k = 2;
        System.out.println("Maximum sum of lengths of subarrays with " + k + " as the max element: " + maxSumOfLengthsWithK(arr, k)); // Output: 6

        int[] arr2 = {5, 1, 3, 4, 2};
        int k2 = 4;
        System.out.println("Maximum sum of lengths of subarrays with " + k2 + " as the max element: " + maxSumOfLengthsWithK(arr2, k2)); // Output: 2

        int[] arr3 = {2, 1, 3, 4, 4};
        int k3 = 4;
        System.out.println("Maximum sum of lengths of subarrays with " + k3 + " as the max element: " + maxSumOfLengthsWithK(arr3, k3)); // Output: 2
    }
}
