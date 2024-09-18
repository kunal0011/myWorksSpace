package amazon;

public class MOnotonicArtray896 {
    public boolean isMonotonic(int[] A) {
        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 1; i < A.length; i++) {
            if (A[i] > A[i - 1]) {
                decreasing = false;
            }
            if (A[i] < A[i - 1]) {
                increasing = false;
            }
        }

        return increasing || decreasing;
    }

    // Test cases
    public static void main(String[] args) {
        MOnotonicArtray896 sol = new MOnotonicArtray896();

        // Test case 1
        int[] A1 = {1, 2, 2, 3};
        System.out.println(sol.isMonotonic(A1));  // Expected output: True

        // Test case 2
        int[] A2 = {6, 5, 4, 4};
        System.out.println(sol.isMonotonic(A2));  // Expected output: True

        // Test case 3
        int[] A3 = {1, 3, 2};
        System.out.println(sol.isMonotonic(A3));  // Expected output: False
    }
}
