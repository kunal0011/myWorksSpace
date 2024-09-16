package amazon;

public class CheckIfValidParenthesis2116 {
public boolean canBeValid(String s, String locked) {
        // If the string length is odd, it can never be a valid parentheses string.
        if (s.length() % 2 != 0) {
        return false;
        }

        // Left-to-right scan
        int openCount = 0;
        int flexibleCount = 0;

        for (int i = 0; i < s.length(); i++) {
        if (locked.charAt(i) == '0') {
        flexibleCount++;  // Treat flexible positions as '(' or ')'
        } else if (s.charAt(i) == '(') {
        openCount++;
        } else {
        openCount--;
        }

        if (openCount < -flexibleCount) {
        return false;
        }
        }

        // Right-to-left scan
        int closeCount = 0;
        flexibleCount = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
        if (locked.charAt(i) == '0') {
        flexibleCount++;
        } else if (s.charAt(i) == ')') {
        closeCount++;
        } else {
        closeCount--;
        }

        if (closeCount < -flexibleCount) {
        return false;
        }
        }

        return true;
        }

public static void main(String[] args) {
        CheckIfValidParenthesis2116 sol = new CheckIfValidParenthesis2116();
        String s = "())()";
        String locked = "00000";
        System.out.println(sol.canBeValid(s, locked));  // Expected output: True
        }
        }
