package miscellaneous;

public class MaximumRepeatingNumber {

    public static int maxRepeating(int[] arr, int n) {
        // Step 1: Increment the value at index arr[i] % n by n
        for (int i = 0; i < n; i++) {
            arr[arr[i] % n] += n;
        }

        // Step 2: Find the index with the maximum value
        int max = arr[0], result = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i] > max) {
                max = arr[i];
                result = i;
            }
        }

        // Step 3: Restore the original array values (optional, if required)
        for (int i = 0; i < n; i++) {
            arr[i] = arr[i] % n;
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {2, 3, 3, 2, 5, 2, 3};
        int n = arr.length;
        System.out.println("The maximum repeating number is: " + maxRepeating(arr, n)); // Output: 3
    }
}
