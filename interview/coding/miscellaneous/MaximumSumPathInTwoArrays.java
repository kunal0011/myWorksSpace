package miscellaneous;

public class MaximumSumPathInTwoArrays {

    public static int maxSumPath(int[] arr1, int[] arr2) {
        int m = arr1.length;
        int n = arr2.length;

        int i = 0, j = 0;
        int sum1 = 0, sum2 = 0;
        int result = 0;

        while (i < m && j < n) {
            if (arr1[i] < arr2[j]) {
                sum1 += arr1[i];
                i++;
            } else if (arr1[i] > arr2[j]) {
                sum2 += arr2[j];
                j++;
            } else {
                // Common element found
                result += Math.max(sum1, sum2);
                sum1 = 0;
                sum2 = 0;

                // Include the common element in the result
                result += arr1[i];
                i++;
                j++;
            }
        }

        // Add remaining elements of arr1
        while (i < m) {
            sum1 += arr1[i];
            i++;
        }

        // Add remaining elements of arr2
        while (j < n) {
            sum2 += arr2[j];
            j++;
        }

        // Add the maximum of the remaining sums
        result += Math.max(sum1, sum2);

        return result;
    }

    public static void main(String[] args) {
        int[] arr1 = {2, 3, 7, 10, 12};
        int[] arr2 = {1, 5, 7, 8};
        System.out.println("Maximum sum path: " + maxSumPath(arr1, arr2)); // Output: 35

        int[] arr3 = {10, 12};
        int[] arr4 = {5, 7, 9};
        System.out.println("Maximum sum path: " + maxSumPath(arr3, arr4)); // Output: 22

        int[] arr5 = {1, 2, 4, 5, 6};
        int[] arr6 = {3, 4, 5, 7};
        System.out.println("Maximum sum path: " + maxSumPath(arr5, arr6)); // Output: 18
    }
}
