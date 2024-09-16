package amazon;

 import java.util.Stack;

public class Finalprice1475 {
    public int[] finalPrices(int[] prices) {
        Stack<Integer> stack = new Stack<>();
        int[] result = prices.clone();

        for (int i = 0; i < prices.length; i++) {
            while (!stack.isEmpty() && prices[stack.peek()] >= prices[i]) {
                int index = stack.pop();
                result[index] = prices[index] - prices[i];
            }
            stack.push(i);
        }

        return result;
    }

    // Testing
    public static void main(String[] args) {
        Finalprice1475 solution = new Finalprice1475();
        int[] prices = {8, 4, 6, 2, 3};
        int[] result = solution.finalPrices(prices);
        System.out.print("Java Test Result: ");
        for (int price : result) {
            System.out.print(price + " ");
        }
        // Output should be [4, 2, 4, 2, 3]
    }
}
