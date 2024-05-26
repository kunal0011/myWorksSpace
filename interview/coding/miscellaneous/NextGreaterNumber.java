package miscellaneous;
import java.util.Arrays;

public class NextGreaterNumber {

    public static int[] findNextGreater(int[] digits) {
        int n = digits.length;

        // Step 1: Find the rightmost pair (i, j) where digits[i] < digits[j]
        int i = n - 2;
        while (i >= 0 && digits[i] >= digits[i + 1]) {
            i--;
        }

        // If no such pair is found, the digits are in descending order
        if (i < 0) {
            return digits; // Return the same array if no greater number is possible
        }

        // Step 2: Find the smallest digit on right side of (i) which is larger than digits[i]
        int j = n - 1;
        while (digits[j] <= digits[i]) {
            j--;
        }

        // Step 3: Swap digits[i] with digits[j]
        swap(digits, i, j);

        // Step 4: Reverse the digits after index i
        reverse(digits, i + 1, n - 1);

        return digits;
    }

    private static void swap(int[] digits, int i, int j) {
        int temp = digits[i];
        digits[i] = digits[j];
        digits[j] = temp;
    }

    private static void reverse(int[] digits, int start, int end) {
        while (start < end) {
            swap(digits, start, end);
            start++;
            end--;
        }
    }

    public static void main(String[] args) {
        int[] digits = {5,3,4,9,7,6};
        int[] result = findNextGreater(digits);
        System.out.println("Next greater number: " + Arrays.toString(result)); // Output: [1, 3, 2]

        int[] digits2 = {3, 2, 1};
        int[] result2 = findNextGreater(digits2);
        System.out.println("Next greater number: " + Arrays.toString(result2)); // Output: [3, 2, 1]

        int[] digits3 = {1, 1, 5};
        int[] result3 = findNextGreater(digits3);
        System.out.println("Next greater number: " + Arrays.toString(result3)); // Output: [1, 5, 1]
    }
}
