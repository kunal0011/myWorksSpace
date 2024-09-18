package amazon;

public class ValidMountainArray941 {
    public boolean validMountainArray(int[] arr) {
        int n = arr.length;
        if (n < 3) {
            return false;
        }

        int i = 0;

        // Climb up to the peak
        while (i + 1 < n && arr[i] < arr[i + 1]) {
            i++;
        }

        // If we never climbed or we are at the last element, it's not a mountain
        if (i == 0 || i == n - 1) {
            return false;
        }

        // Climb down from the peak
        while (i + 1 < n && arr[i] > arr[i + 1]) {
            i++;
        }

        // Check if we've reached the end of the array
        return i == n - 1;
    }

    // Test cases
    public static void main(String[] args) {
        ValidMountainArray941 sol = new ValidMountainArray941();

        // Test case 1
        int[] arr1 = {2, 1};
        System.out.println(sol.validMountainArray(arr1));  // Expected output: False

        // Test case 2
        int[] arr2 = {3, 5, 5};
        System.out.println(sol.validMountainArray(arr2));  // Expected output: False

        // Test case 3
        int[] arr3 = {0, 3, 2, 1};
        System.out.println(sol.validMountainArray(arr3));  // Expected output: True
    }
}
