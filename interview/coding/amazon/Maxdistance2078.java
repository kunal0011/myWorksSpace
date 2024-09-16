package amazon;

public class Maxdistance2078 {
    public int maxDistance(int[] colors) {
        int n = colors.length;

        // Maximum distance variables
        int maxDistStart = 0;
        int maxDistEnd = 0;

        // From start to end
        for (int i = 0; i < n; i++) {
            if (colors[i] != colors[n - 1]) {  // Compare with last element
                maxDistStart = Math.max(maxDistStart, n - 1 - i);
            }
        }

        // From end to start
        for (int i = n - 1; i >= 0; i--) {
            if (colors[i] != colors[0]) {  // Compare with first element
                maxDistEnd = Math.max(maxDistEnd, i);
            }
        }

        return Math.max(maxDistStart, maxDistEnd);
    }

    // Testing the solution
    public static void main(String[] args) {
        Maxdistance2078 solution = new Maxdistance2078();

        // Test case
        int[] colors = {1, 1, 2, 3, 2, 1};
        System.out.println("Maximum Distance: " + solution.maxDistance(colors));  // Expected output: 4
    }
}
