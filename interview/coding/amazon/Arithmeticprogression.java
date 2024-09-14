package amazon;

import java.util.Arrays;

public class Arithmeticprogression {
    public boolean canMakeArithmeticProgression(int[] arr) {
        // Sort the array first
        Arrays.sort(arr);

        // Find the difference between the first two elements
        int diff = arr[1] - arr[0];

        // Check if every consecutive pair has the same difference
        for (int i = 2; i < arr.length; i++) {
            if (arr[i] - arr[i - 1] != diff) {
                return false;
            }
        }

        return true;
    }

}
