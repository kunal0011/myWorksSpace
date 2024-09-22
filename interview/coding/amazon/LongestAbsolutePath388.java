package amazon;

import java.util.Stack;

public class LongestAbsolutePath388 {
    public int lengthLongestPath(String input) {
        // Stack to store the current path length at each depth
        Stack<Integer> stack = new Stack<>();
        int maxLen = 0;

        // Split the input by newlines to process each line (directory or file)
        String[] lines = input.split("\n");

        for (String line : lines) {
            // Count the depth of the current directory or file (number of tabs)
            int depth = line.lastIndexOf("\t") + 1;
            // Remove the tabs to get the actual name
            String name = line.substring(depth);

            // Pop from the stack if the stack is larger than the current depth
            while (stack.size() > depth) {
                stack.pop();
            }

            if (name.contains(".")) {
                // It's a file, calculate the total path length
                int currentLength = (stack.isEmpty() ? 0 : stack.peek()) + name.length();
                maxLen = Math.max(maxLen, currentLength);
            } else {
                // It's a directory, push its length onto the stack
                int length = (stack.isEmpty() ? 0 : stack.peek()) + name.length() + 1; // +1 for the "/"
                stack.push(length);
            }
        }

        return maxLen;
    }

    // Test cases
    public static void main(String[] args) {
        LongestAbsolutePath388 sol = new LongestAbsolutePath388();

        // Test case 1
        String input1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext";
        System.out.println(sol.lengthLongestPath(input1));  // Output: 20

        // Test case 2
        String input2 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext\n\tsubdir3";
        System.out.println(sol.lengthLongestPath(input2));  // Output: 20

        // Test case 3
        String input3 = "dir\n\tsubdir1\n\t\tfile1.ext\n\tsubdir2\n\t\tfile2.ext";
        System.out.println(sol.lengthLongestPath(input3));  // Output: 21
    }
}
