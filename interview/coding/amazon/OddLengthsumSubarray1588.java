package amazon;

public class OddLengthsumSubarray1588 {
    public int sumOddLengthSubarrays(int[] arr) {
        int totalSum = 0;
        int n = arr.length;

        // Iterate through each element
        for (int i = 0; i < n; i++) {
            // Calculate contribution of arr[i] to all odd-length subarrays
            int left = i + 1;  // Number of subarrays ending at or before index i
            int right = n - i; // Number of subarrays starting at or after index i

            // Total subarrays that include arr[i]
            int totalSubarrays = left * right;

            // Odd-length subarrays that include arr[i]
            int oddSubarrays = (totalSubarrays + 1) / 2;

            // Add the contribution of arr[i] to the total sum
            totalSum += oddSubarrays * arr[i];
        }

        return totalSum;
    }

    // Testing
    public static void main(String[] args) {
        OddLengthsumSubarray1588 solution = new OddLengthsumSubarray1588();
        int[] arr = {1, 4, 2, 5, 3};
        System.out.println("Java Test Result: " + solution.sumOddLengthSubarrays(arr));  // Output should be 58
    }
}

