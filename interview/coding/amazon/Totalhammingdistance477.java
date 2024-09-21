package amazon;

public class Totalhammingdistance477 {
    public int totalHammingDistance(int[] nums) {
        int totalDistance = 0;
        int n = nums.length;

        // There are at most 32 bits to consider (for 32-bit integers)
        for (int bitPosition = 0; bitPosition < 32; bitPosition++) {
            int countOnes = 0;

            // Count how many numbers have a 1 at the current bit position
            for (int num : nums) {
                if ((num >> bitPosition & 1) == 1) {
                    countOnes++;
                }
            }

            int countZeros = n - countOnes;
            // The Hamming distance contribution from this bit position
            totalDistance += countOnes * countZeros;
        }

        return totalDistance;
    }

    // Test cases
    public static void main(String[] args) {
        Totalhammingdistance477 sol = new Totalhammingdistance477();

        // Test case 1
        int[] nums1 = {4, 14, 2};
        System.out.println(sol.totalHammingDistance(nums1));  // Expected output: 6

        // Test case 2
        int[] nums2 = {1, 2, 3};
        System.out.println(sol.totalHammingDistance(nums2));  // Expected output: 4
    }
}

