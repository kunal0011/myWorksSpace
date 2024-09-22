package amazon;

 import java.util.Arrays;

public class Heaters475 {
    public int findRadius(int[] houses, int[] heaters) {
        // Sort both the houses and heaters arrays
        Arrays.sort(houses);
        Arrays.sort(heaters);
        int maxRadius = 0;

        // For each house, find the minimum distance to a heater
        for (int house : houses) {
            // Find the closest heater using binary search
            int idx = Arrays.binarySearch(heaters, house);

            // If the house is at a heater's position
            if (idx >= 0) {
                continue;
            }

            // If not found, binarySearch returns (-insertion point - 1)
            idx = -idx - 1;

            // Calculate distances to the closest heaters on both sides
            int distLeft = (idx == 0) ? Integer.MAX_VALUE : house - heaters[idx - 1];
            int distRight = (idx == heaters.length) ? Integer.MAX_VALUE : heaters[idx] - house;

            // Take the smaller of the two distances
            int minDist = Math.min(distLeft, distRight);

            // Track the maximum of the minimum distances (the required radius)
            maxRadius = Math.max(maxRadius, minDist);
        }

        return maxRadius;
    }

    // Test cases
    public static void main(String[] args) {
        Heaters475 sol = new Heaters475();

        // Test case 1
        int[] houses1 = {1, 2, 3};
        int[] heaters1 = {2};
        System.out.println(sol.findRadius(houses1, heaters1));  // Expected output: 1

        // Test case 2
        int[] houses2 = {1, 2, 3, 4};
        int[] heaters2 = {1, 4};
        System.out.println(sol.findRadius(houses2, heaters2));  // Expected output: 1

        // Test case 3
        int[] houses3 = {1, 5};
        int[] heaters3 = {2};
        System.out.println(sol.findRadius(houses3, heaters3));  // Expected output: 3
    }
}

