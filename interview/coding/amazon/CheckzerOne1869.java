package amazon;

public class CheckzerOne1869 {
    public boolean checkZeroOnes(String s) {
        int maxOnes = 0, maxZeros = 0;
        int currentOnes = 0, currentZeros = 0;

        // Traverse the string
        for (char c : s.toCharArray()) {
            if (c == '1') {
                currentOnes++;
                currentZeros = 0;  // Reset zeros
            } else {
                currentZeros++;
                currentOnes = 0;  // Reset ones
            }

            maxOnes = Math.max(maxOnes, currentOnes);  // Update max ones
            maxZeros = Math.max(maxZeros, currentZeros);  // Update max zeros
        }

        // Return True if the longest 1-segment is longer than the longest 0-segment
        return maxOnes > maxZeros;
    }

    // Testing the solution
    public static void main(String[] args) {
        CheckzerOne1869 solution = new CheckzerOne1869();

        // Test case
        String s = "1101";
        System.out.println("Longer ones than zeros: " + solution.checkZeroOnes(s));  // Expected output: True
    }
}

