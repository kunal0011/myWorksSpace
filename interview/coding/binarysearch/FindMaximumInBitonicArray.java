package binarysearch;

public class FindMaximumInBitonicArray {

    public static int findMaximum(int[] arr) {
        int start = 0;
        int end = arr.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            // Check if mid is the peak element
            if ((mid == 0 || arr[mid] > arr[mid - 1]) &&
                    (mid == arr.length - 1 || arr[mid] > arr[mid + 1])) {
                return arr[mid];
            }

            // If mid is not the peak and mid is greater than the next element
            if (mid < arr.length - 1 && arr[mid] > arr[mid + 1]) {
                // The peak lies on the left side
                end = mid - 1;
            } else {
                // The peak lies on the right side
                start = mid + 1;
            }
        }

        // This return is just to satisfy the compiler. The function should never reach here.
        return -1;
    }

    public static void main(String[] args) {
        int[] arr1 = {1, 3, 8, 12, 4, 2};
        System.out.println("Maximum element is: " + findMaximum(arr1)); // Output: 12

        int[] arr2 = {3, 9, 10, 20, 17, 5, 1};
        System.out.println("Maximum element is: " + findMaximum(arr2)); // Output: 20

        int[] arr3 = {10, 20, 30, 40, 50, 60, 70, 60, 50, 40, 30};
        System.out.println("Maximum element is: " + findMaximum(arr3)); // Output: 70
    }
}
