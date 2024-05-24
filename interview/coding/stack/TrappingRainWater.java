package stack;

import java.util.Stack;

public class TrappingRainWater {

    public static int trap(int[] height) {
        if (height == null || height.length == 0) {
            return 0;
        }

        Stack<Integer> stack = new Stack<>();
        int totalWater = 0;
        int current = 0;

        while (current < height.length) {
            while (!stack.isEmpty() && height[current] > height[stack.peek()]) {
                int top = stack.pop();
                if (stack.isEmpty()) {
                    break;
                }
                int distance = current - stack.peek() - 1;
                int boundedHeight = Math.min(height[current], height[stack.peek()]) - height[top];
                totalWater += distance * boundedHeight;
            }
            stack.push(current++);
        }

        return totalWater;
    }

    public static void main(String[] args) {
       // int[] height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        int [] height = {3,0,2,0,4};
        System.out.println("Total water trapped: " + trap(height));
    }
}
