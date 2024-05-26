package miscellaneous;

public class MaxSumNoAdjacent {

    public static int maxSumNonAdjacent(int[] arr) {
        if (arr == null || arr.length == 0) {
            return 0;
        }

        int include = arr[0];  // Sum including the first element
        int exclude = 0;       // Sum excluding the first element

        for (int i = 1; i < arr.length; i++) {
            int newExclude = Math.max(include, exclude); // Exclude current element
            include = exclude + arr[i]; // Include current element
            exclude = newExclude;
        }

        // Maximum of including or excluding the last element
        return Math.max(include, exclude);
    }

    public static void main(String[] args) {
        int[] arr1 = {3, 2, 5, 10, 7};
        System.out.println("Maximum sum of non-adjacent elements: " + maxSumNonAdjacent(arr1)); // Output: 15

        int[] arr2 = {3, 2, 7, 10};
        System.out.println("Maximum sum of non-adjacent elements: " + maxSumNonAdjacent(arr2)); // Output: 13

        int[] arr3 = {5, 5, 10, 100, 10, 5};
        System.out.println("Maximum sum of non-adjacent elements: " + maxSumNonAdjacent(arr3)); // Output: 110

        int[] arr4 = {1, 2, 3};
        System.out.println("Maximum sum of non-adjacent elements: " + maxSumNonAdjacent(arr4)); // Output: 4
    }
}
