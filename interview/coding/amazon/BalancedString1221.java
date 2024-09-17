package amazon;

public class BalancedString1221 {
    public int balancedStringSplit(String s) {
        int balance = 0;
        int count = 0;

        // Traverse through the string
        for (char c : s.toCharArray()) {
            // Increase balance for 'L', decrease for 'R'
            if (c == 'L') {
                balance++;
            } else {
                balance--;
            }

            // When balance is 0, we found a balanced string
            if (balance == 0) {
                count++;
            }
        }

        return count;
    }

    // Test cases
    public static void main(String[] args) {
        BalancedString1221 sol = new BalancedString1221();

        // Test case 1
        String s1 = "RLRRLLRLRL";
        int result1 = sol.balancedStringSplit(s1);
        assert result1 == 4 : "Test case 1 failed: " + result1;

        // Test case 2
        String s2 = "RLLLLRRRLR";
        int result2 = sol.balancedStringSplit(s2);
        assert result2 == 3 : "Test case 2 failed: " + result2;

        // Test case 3
        String s3 = "LLLLRRRR";
        int result3 = sol.balancedStringSplit(s3);
        assert result3 == 1 : "Test case 3 failed: " + result3;

        System.out.println("All test cases passed!");
    }
}
