package amazon;

public class Uniquebinarystring1980 {
    public String findDifferentBinaryString(String[] nums) {
        int n = nums.length;
        StringBuilder result = new StringBuilder();

        // Build the binary string using Cantor's diagonalization
        for (int i = 0; i < n; i++) {
            // Flip the ith character of the ith string (0 -> 1, 1 -> 0)
            if (nums[i].charAt(i) == '0') {
                result.append('1');
            } else {
                result.append('0');
            }
        }

        return result.toString();
    }

    // Testing the solution
    public static void main(String[] args) {
        Uniquebinarystring1980 solution = new Uniquebinarystring1980();

        // Test case
        String[] nums = {"111", "011", "001"};
        System.out.println("Unique Binary String: " + solution.findDifferentBinaryString(nums));  // Expected output: "100"
    }
}

