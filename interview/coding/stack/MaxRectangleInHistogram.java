package stack;

import java.util.Stack;

public class MaxRectangleInHistogram {

    public static int getMaxArea(int[] hist) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        int tp;  // Top of stack
        int areaWithTop; // Area with top bar as the smallest (or minimum height) bar

        int i = 0;
        while (i < hist.length) {
            // If this bar is higher than the bar at stack top, push it to the stack
            if (stack.isEmpty() || hist[stack.peek()] <= hist[i]) {
                stack.push(i++);
            } else {
                // Pop the top
                tp = stack.pop();

                // Calculate the area with hist[tp] as the smallest (or minimum height) bar
                areaWithTop = hist[tp] * (stack.isEmpty() ? i : i - stack.peek() - 1);

                // Update maxArea, if needed
                if (maxArea < areaWithTop) {
                    maxArea = areaWithTop;
                }
            }
        }

        // Now, pop the remaining bars from stack and calculate area
        while (!stack.isEmpty()) {
            tp = stack.pop();
            areaWithTop = hist[tp] * (stack.isEmpty() ? i : i - stack.peek() - 1);

            if (maxArea < areaWithTop) {
                maxArea = areaWithTop;
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        int[] hist = {6, 2, 5, 4, 5, 1, 6};
        //int[] hist = {2,4,5,6,7};
        System.out.println("Maximum rectangular area in histogram is " + getMaxArea(hist));
    }
}
