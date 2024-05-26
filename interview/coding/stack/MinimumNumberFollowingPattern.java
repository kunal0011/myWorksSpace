package stack;

import java.util.Stack;

public class MinimumNumberFollowingPattern {

    public static String minNumber(String pattern) {
        // Initialize an empty stack and an empty result string
        Stack<Integer> stack = new Stack<>();
        StringBuilder result = new StringBuilder();

        // Initialize the first digit to push onto the stack
        int nextAvailable = 1;

        // Process each character in the pattern
        for (int i = 0; i <= pattern.length(); i++) {
            // If 'I' or end of pattern, push the next available digit onto the stack
            if (i == pattern.length() || pattern.charAt(i) == 'I') {
                stack.push(nextAvailable++);

                // Process any consecutive 'D's and append the popped digits to the result
                while (!stack.isEmpty()) {
                    result.append(stack.pop());
                }
            } else {
                // If 'D', just push the current value of 'nextAvailable' onto the stack
                stack.push(nextAvailable++);
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        String pattern1 = "IDID";
        System.out.println("Minimum number following pattern " + pattern1 + ": " + minNumber(pattern1)); // Output: 13254

        String pattern2 = "I";
        System.out.println("Minimum number following pattern " + pattern2 + ": " + minNumber(pattern2)); // Output: 12

        String pattern3 = "DD";
        System.out.println("Minimum number following pattern " + pattern3 + ": " + minNumber(pattern3)); // Output: 321

        String pattern4 = "DIDI";
        System.out.println("Minimum number following pattern " + pattern4 + ": " + minNumber(pattern4)); // Output: 3214
    }
}
