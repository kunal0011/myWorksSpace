package amazon;

public class MonotoneIncreasingDigits738 {
    public int monotoneIncreasingDigits(int N) {
        char[] digits = Integer.toString(N).toCharArray();
        int mark = digits.length;  // Mark where to set digits to '9'

        // Traverse the digits from right to left
        for (int i = digits.length - 1; i > 0; i--) {
            if (digits[i] < digits[i - 1]) {  // Find where the monotone property is broken
                mark = i;
                digits[i - 1]--;  // Decrease the problematic digit
            }
        }

        // Set all digits after the mark to '9'
        for (int i = mark; i < digits.length; i++) {
            digits[i] = '9';
        }

        return Integer.parseInt(new String(digits));  // Convert the array of digits back to an integer
    }
}

