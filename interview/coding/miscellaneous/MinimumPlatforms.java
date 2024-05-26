package miscellaneous;

import java.util.Arrays;

public class MinimumPlatforms {
    public static int findPlatform(int[] arr, int[] dep, int n) {
        // Sort arrival and departure arrays
        Arrays.sort(arr);
        Arrays.sort(dep);

        // Initialize pointers for arrival and departure arrays
        int platform_needed = 1, max_platforms = 1;
        int i = 1, j = 0;

        // Traverse the arrival and departure arrays
        while (i < n && j < n) {
            // If the next event is an arrival, increment count of platforms needed
            if (arr[i] <= dep[j]) {
                platform_needed++;
                i++;
            }
            // If the next event is a departure, decrement count of platforms needed
            else {
                platform_needed--;
                j++;
            }
            // Update the maximum platforms needed
            if (platform_needed > max_platforms) {
                max_platforms = platform_needed;
            }
        }

        return max_platforms;
    }

    public static void main(String[] args) {
        int[] arr = {900, 940, 950, 1100, 1500, 1800};
        int[] dep = {910, 1200, 1120, 1130, 1900, 2000};
        int n = arr.length;
        System.out.println("Minimum number of platforms required: " + findPlatform(arr, dep, n)); // Output: 3
    }
}
