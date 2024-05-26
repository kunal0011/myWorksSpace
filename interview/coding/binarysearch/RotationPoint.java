package binarysearch;

public class RotationPoint {

    public static int findRotationPoint(int[] arr) {
        int low = 0;
        int high = arr.length - 1;

        // Handle cases where the array is not rotated
        if (arr[low] < arr[high]) {
            return low;  // The array is already sorted and not rotated
        }

        while (low < high) {
            int mid = low + (high - low) / 2;

            // Check if mid is the rotation point
            if (arr[mid] > arr[mid + 1]) {
                return mid + 1;
            }

            if (arr[mid] < arr[mid - 1]) {
                return mid;
            }

            // Decide which half to choose
            if (arr[mid] > arr[low]) {
                // The rotation point is in the right half
                low = mid + 1;
            } else {
                // The rotation point is in the left half
                high = mid - 1;
            }
        }

        return low;
    }

    public static void main(String[] args) {
        int[] arr1 = {4, 5, 6, 7, 0, 1, 2};
        System.out.println("Rotation point index: " + findRotationPoint(arr1)); // Output: 4

        int[] arr2 = {10, 15, 1, 3, 8};
        System.out.println("Rotation point index: " + findRotationPoint(arr2)); // Output: 2

        int[] arr3 = {3, 4, 5, 6, 1, 2};
        System.out.println("Rotation point index: " + findRotationPoint(arr3)); // Output: 4
    }
}
