package amazon;

public class Maxchunktomakesorted769 {
    public int maxChunksToSorted(int[] arr) {
        int maxSoFar = 0;
        int chunks = 0;

        for (int i = 0; i < arr.length; i++) {
            maxSoFar = Math.max(maxSoFar, arr[i]);  // Track the maximum value in the chunk
            if (maxSoFar == i) {  // If the maximum value matches the index, we can make a chunk
                chunks++;
            }
        }

        return chunks;
    }

    // Test cases
    public static void main(String[] args) {
        Maxchunktomakesorted769 sol = new Maxchunktomakesorted769();

        // Test case 1
        int[] arr1 = {4, 3, 2, 1, 0};
        System.out.println(sol.maxChunksToSorted(arr1));  // Expected output: 1

        // Test case 2
        int[] arr2 = {1, 0, 2, 3, 4};
        System.out.println(sol.maxChunksToSorted(arr2));  // Expected output: 4
    }
}
