package miscellaneous;

import java.util.LinkedList;
import java.util.Queue;

public class JumpingNumbers {
    public static void printJumpingNumbers(int limit) {
        // Add single-digit numbers to the queue
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= 9 && i <= limit; i++) {
            queue.offer(i);
        }

        // BFS traversal
        while (!queue.isEmpty()) {
            int num = queue.poll();
            if (num <= limit) {
                System.out.print(num + " ");
            }

            // Extract the last digit
            int lastDigit = num % 10;

            // Check if we can append the next digit
            if (lastDigit < 9 && num * 10 + (lastDigit + 1) <= limit) {
                queue.offer(num * 10 + (lastDigit + 1));
            }

            // Check if we can append the previous digit
            if (lastDigit > 0 && num * 10 + (lastDigit - 1) <= limit) {
                queue.offer(num * 10 + (lastDigit - 1));
            }
        }
    }

    public static void main(String[] args) {
        int limit = 40;
        System.out.println("Jumping numbers smaller than or equal to " + limit + ":");
        printJumpingNumbers(limit);
    }
}
