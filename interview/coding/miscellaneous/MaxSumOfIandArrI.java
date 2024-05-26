package miscellaneous;

public class MaxSumOfIandArrI {
// Maximum sum of i*arr[i] among all rotations of a given array
    public static int maxSumOfIandArrI(int[] arr) {
        int n = arr.length;

        // Calculate S0 (the initial sum of i * arr[i])
        int currentSum = 0;
        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            currentSum += i * arr[i];
            totalSum += arr[i];
        }

        int maxSum = currentSum;

        // Calculate sums for other rotations and track the maximum
        for (int k = 1; k < n; k++) {
            // Use the relation: S_k = S_{k-1} + totalSum - n * arr[n-k]
            currentSum = currentSum + totalSum - n * arr[n - k];
            if (currentSum > maxSum) {
                maxSum = currentSum;
            }
        }

        return maxSum;
    }

    public static void main(String[] args) {
        int[] arr = {8, 3, 1, 2};
        System.out.println("Maximum sum of i*arr[i] among all rotations: " + maxSumOfIandArrI(arr)); // Output: 29

        int[] arr2 = {1, 20, 2, 10};
        System.out.println("Maximum sum of i*arr[i] among all rotations: " + maxSumOfIandArrI(arr2)); // Output: 72
    }
}
