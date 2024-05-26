package miscellaneous;

public class UniqueElementFinder {
//Given an array where every element occurs three times, except one element which occurs only once. Find the element that occurs once.
//    Bitwise Counting: For each bit position (from 0 to 31, assuming 32-bit integers), count how many numbers have the bit set at that position.
//    Modulo Operation: If a bit position has a count that is not a multiple of three, it means the unique element has a bit set at that position.
// Given an array where every element occurs three times, except one element which occurs only once. Find the element that occurs once.
    public static int findUniqueElement(int[] arr) {
        int[] bitCount = new int[32]; // Array to hold the count of bits

        // Count the number of set bits at each position
        for (int num : arr) {
            for (int i = 0; i < 32; i++) {
                bitCount[i] += (num >> i) & 1;
            }
        }

        // Reconstruct the unique number from bit counts
        int result = 0;
        for (int i = 0; i < 32; i++) {
            if (bitCount[i] % 3 != 0) {
                result |= (1 << i);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr1 = {2, 2, 3, 2};
        System.out.println("Unique element is: " + findUniqueElement(arr1)); // Output: 3

        int[] arr2 = {0, 1, 0, 1, 0, 1, 99};
        System.out.println("Unique element is: " + findUniqueElement(arr2)); // Output: 99
    }
}
