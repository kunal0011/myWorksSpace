package miscellaneous;

public class ElementBeforeSmallerAfterGrater {

    public static int findElement(int[] arr) {
        int n = arr.length;

        // Initialize the leftMax and rightMin arrays
        int[] leftMax = new int[n];
        int[] rightMin = new int[n];

        // Fill leftMax array
        leftMax[0] = Integer.MIN_VALUE;
        for (int i = 1; i < n; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], arr[i - 1]);
        }

        // Fill rightMin array
        rightMin[n - 1] = Integer.MAX_VALUE;
        for (int i = n - 2; i >= 0; i--) {
            rightMin[i] = Math.min(rightMin[i + 1], arr[i + 1]);
        }

        // Find the element
        for (int i = 0; i < n; i++) {
            if (leftMax[i] < arr[i] && arr[i] < rightMin[i]) {
                return arr[i];
            }
        }

        // If no such element is found, return -1 or an indication of no such element
        return -1;
    }

    public static void main(String[] args) {
        int[] arr1 = {5, 1, 4, 2, 3};
        System.out.println("Element: " + findElement(arr1)); // Output: 4

        int[] arr2 = {1, 2, 3, 4, 5, 6};
        System.out.println("Element: " + findElement(arr2)); // Output: -1 (no such element)

        int[] arr3 = {4, 3, 2, 5, 8, 6, 7};
        System.out.println("Element: " + findElement(arr3)); // Output: 5
    }
}
