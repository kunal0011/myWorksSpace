package miscellaneous;

public class XorOfSubarrays {
    public static int xorOfAllSubarrays(int[] arr) {
        int n = arr.length;
        int result = 0;

        // Iterate through each element in the array
        for (int i = 0; i < n; i++) {
            // Calculate the number of subarrays that include arr[i]
            int subarrayCount = (i + 1) * (n - i);

            // If the count is odd, include arr[i] in the result
            if (subarrayCount % 2 != 0) {
                result ^= arr[i];
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        int result = xorOfAllSubarrays(arr);
        System.out.println("XOR of all subarrays: " + result); // Output: 4
    }
}
