package amazon;

public class KthMissingPositive1539 {
    public int findKthPositive(int[] arr, int k) {
        int missingCount = 0;
        int currentNum = 1;
        int index = 0;

        while (missingCount < k) {
            // If currentNum is in arr, skip it
            if (index < arr.length && arr[index] == currentNum) {
                index++;
            } else {
                // Otherwise, it's a missing number
                missingCount++;
            }
            // Move to the next number
            currentNum++;
        }

        // Since we overshoot by one in the last iteration
        return currentNum - 1;
    }

    // Testing
    public static void main(String[] args) {
        KthMissingPositive1539 solution = new KthMissingPositive1539();
        int[] arr = {2, 3, 4, 7, 11};
        int k = 5;
        System.out.println("Java Test Result: " + solution.findKthPositive(arr, k));  // Output should be 9
    }
}
