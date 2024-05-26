package miscellaneous;

public class FloorInSortedArray {

    public static int floor(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;
        int floor = -1; // Initialize the floor to -1, indicating no such element found

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // If current element is equal to target, return it as the floor
            if (arr[mid] == target) {
                return arr[mid];
            }
            // If current element is less than target, update floor and search in right half
            else if (arr[mid] < target) {
                floor = arr[mid];
                left = mid + 1;
            }
            // If current element is greater than target, search in left half
            else {
                right = mid - 1;
            }
        }

        return floor;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 6, 8, 10};
        int target = 5;
        int result = floor(arr, target);
        System.out.println("Floor of " + target + " in the array: " + result); // Output: 4
    }
}
