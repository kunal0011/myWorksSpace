package amazon;

public class Arithmeticslice413 {
    public int numberOfArithmeticSlices(int[] A) {
        if (A.length < 3) {
            return 0;
        }

        int count = 0;
        int currentSlices = 0;

        for (int i = 2; i < A.length; i++) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
                currentSlices++;
                count += currentSlices;
            } else {
                currentSlices = 0;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Arithmeticslice413 sol = new Arithmeticslice413();
        System.out.println(sol.numberOfArithmeticSlices(new int[]{1, 2, 3, 4}));  // Expected output: 3
        System.out.println(sol.numberOfArithmeticSlices(new int[]{1}));           // Expected output: 0
        System.out.println(sol.numberOfArithmeticSlices(new int[]{1, 3, 5, 7, 9})); // Expected output: 6
    }
}

