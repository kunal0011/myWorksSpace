package amazon;

 import java.lang.Math;

public class SumOfSquare633 {
    public boolean judgeSquareSum(int c) {
        // Initialize two pointers
        int a = 0;
        int b = (int) Math.sqrt(c);  // b starts from the square root of c

        // Use two pointers to check if a^2 + b^2 = c
        while (a <= b) {
            int sumOfSquares = a * a + b * b;
            if (sumOfSquares == c) {
                return true;
            } else if (sumOfSquares < c) {
                a++;
            } else {
                b--;
            }
        }

        return false;
    }

    // Test cases
    public static void main(String[] args) {
        SumOfSquare633 sol = new SumOfSquare633();

        // Test case 1
        int c1 = 5;
        System.out.println(sol.judgeSquareSum(c1));  // Output: true

        // Test case 2
        int c2 = 3;
        System.out.println(sol.judgeSquareSum(c2));  // Output: false

        // Test case 3
        int c3 = 4;
        System.out.println(sol.judgeSquareSum(c3));  // Output: true
    }
}

