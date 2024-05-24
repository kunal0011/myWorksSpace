package stack;

import java.util.Stack;

import java.util.Stack;

public class StockSpanProblem {

    public static int[] calculateSpan(int[] prices) {
        int n = prices.length;
        int[] span = new int[n];
        Stack<Integer> stack = new Stack<>();

        // Initialize the first span value
        span[0] = 1;
        stack.push(0);

        // Calculate span values for the rest of the days
        for (int i = 1; i < n; i++) {
            // Pop elements from stack while stack is not empty and top of stack is less than or equal to current price
            while (!stack.isEmpty() && prices[stack.peek()] <= prices[i]) {
                stack.pop();
            }

            // If stack becomes empty, then price[i] is greater than all elements to the left
            span[i] = (stack.isEmpty()) ? (i + 1) : (i - stack.peek());

            // Push this element's index to the stack
            stack.push(i);
        }

        return span;
    }

    public static void main(String[] args) {
        int[] prices = {100, 80, 60, 70, 60, 75, 85};
        int[] span = calculateSpan(prices);

        System.out.println("Stock prices: ");
        for (int price : prices) {
            System.out.print(price + " ");
        }
        System.out.println();

        System.out.println("Span values: ");
        for (int s : span) {
            System.out.print(s + " ");
        }
        System.out.println();
    }
}
