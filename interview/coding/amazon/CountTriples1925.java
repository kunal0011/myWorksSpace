package amazon;

public class CountTriples1925 {
    public int countTriples(int n) {
        int count = 0;

        // Iterate through all values of a, b, c
        for (int c = 1; c <= n; c++) {
            for (int a = 1; a < c; a++) {
                for (int b = a; b < c; b++) {
                    if (a * a + b * b == c * c) {
                        count += 2;  // (a, b, c) and (b, a, c) are both valid
                    }
                }
            }
        }

        return count;
    }

    // Testing the solution
    public static void main(String[] args) {
        CountTriples1925 solution = new CountTriples1925();

        // Test case
        int n = 5;
        System.out.println("Count of Square Sum Triples: " + solution.countTriples(n));  // Expected output: 2
    }
}

