package miscellaneous;

import java.util.ArrayList;
import java.util.List;

public class MaxConsecutiveOnes {

    public static List<Integer> findZeroesToFlip(int[] arr, int m) {
        // List to store the positions of zeroes that need to be flipped
        List<Integer> zeroIndices = new ArrayList<>();

        // Variables to keep track of the current window and max window
        int left = 0, right = 0;
        int zeroCount = 0;
        int maxLength = 0;
        int maxLeft = 0;

        // Traverse the array using the right pointer
        while (right < arr.length) {
            // If current element is 0, increment the zero count
            if (arr[right] == 0) {
                zeroCount++;
            }

            // While zero count is more than m, move the left pointer to shrink the window
            while (zeroCount > m) {
                if (arr[left] == 0) {
                    zeroCount--;
                }
                left++;
            }

            // Update the max length and the starting index of the max window
            if (right - left + 1 > maxLength) {
                maxLength = right - left + 1;
                maxLeft = left;
            }

            // Move the right pointer to expand the window
            right++;
        }

        // Collect the indices of zeroes to be flipped in the max window
        for (int i = maxLeft; i < maxLeft + maxLength; i++) {
            if (arr[i] == 0) {
                zeroIndices.add(i);
            }
        }

        return zeroIndices;
    }

    public static void main(String[] args) {
        int[] arr = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1};
        int m = 2;
        List<Integer> result = findZeroesToFlip(arr, m);

        System.out.println("Zeroes to flip to maximize consecutive 1's: " + result);
    }
}
