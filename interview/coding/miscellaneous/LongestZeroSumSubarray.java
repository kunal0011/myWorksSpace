package miscellaneous;

import java.util.HashMap;

public class LongestZeroSumSubarray {

    /*
    * Cumulative Sum: Maintain a cumulative sum while iterating through the array.
HashMap: Use a HashMap to store the first occurrence of each cumulative sum.
Check for Zero Sum: If the cumulative sum is zero at any index, it means the subarray from the start to this index has a sum of 0.
Check for Repeated Sum: If the cumulative sum has been seen before, it means the subarray between the previous occurrence and the current index has a sum of 0.
    *
    *
    *
    *
    * */

    public static int longestZeroSumSubarray(int[] arr) {
        HashMap<Integer, Integer> sumIndexMap = new HashMap<>();
        int maxLength = 0;
        int cumulativeSum = 0;

        for (int i = 0; i < arr.length; i++) {
            cumulativeSum += arr[i];

            // If cumulative sum is zero, we found a subarray from the beginning to i
            if (cumulativeSum == 0) {
                maxLength = i + 1;
            }

            // If cumulative sum has been seen before, there's a subarray with zero sum
            if (sumIndexMap.containsKey(cumulativeSum)) {
                maxLength = Math.max(maxLength, i - sumIndexMap.get(cumulativeSum));
            } else {
                // Store the first occurrence of this cumulative sum
                sumIndexMap.put(cumulativeSum, i);
            }
        }

        return maxLength;
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 2, -2, 4, -4};
        System.out.println("Length of the longest subarray with sum 0: " + longestZeroSumSubarray(arr1)); // Output: 5

        int[] arr2 = {1, 2, 3, -3, 4, -2, -2, 3};
        System.out.println("Length of the longest subarray with sum 0: " + longestZeroSumSubarray(arr2)); // Output: 7

        int[] arr3 = {1, -1, 3, 2, -2, -3, 3, -3};
        System.out.println("Length of the longest subarray with sum 0: " + longestZeroSumSubarray(arr3)); // Output: 8
    }
}
