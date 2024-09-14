package amazon;

public class minimumSum2160 {
    public int minimumSum(int num) {
        // Extract digits
        int[] digits = new int[4];
        for (int i = 0; i < 4; i++) {
            digits[i] = num % 10;
            num /= 10;
        }

        // Sort digits to easily find minimal combinations
        java.util.Arrays.sort(digits);

        // Form two smallest and two largest possible two-digit numbers
        int num1 = digits[0] * 10 + digits[1];
        int num2 = digits[2] * 10 + digits[3];

        return Math.min(num1 + num2,
                digits[0] * 10 + digits[2] + digits[1] * 10 + digits[3]);
    }

    public static void main(String[] args) {
        minimumSum2160 s = new minimumSum2160();
        s.minimumSum(2932);
    }
}
