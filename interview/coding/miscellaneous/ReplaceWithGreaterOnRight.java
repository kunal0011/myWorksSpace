package miscellaneous;

public class ReplaceWithGreaterOnRight {
    public static void replaceWithGreater(int[] arr) {
        int n = arr.length;
        if (n <= 0) return;

        int maxSoFar = arr[n - 1];
        arr[n - 1] = -1; // The last element doesn't have any element on its right side, so replace it with -1.

        for (int i = n - 2; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = maxSoFar;
            maxSoFar = Math.max(maxSoFar, temp);
        }
    }

    public static void main(String[] args) {
        int[] arr = {17, 18, 5, 4, 6, 1};
        System.out.println("Original array:");
        printArray(arr);

        replaceWithGreater(arr);

        System.out.println("Array after replacing with greater element on right side:");
        printArray(arr);
    }

    private static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
