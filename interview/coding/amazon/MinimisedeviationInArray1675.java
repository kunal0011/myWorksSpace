package amazon;

import java.util.PriorityQueue;

public class MinimisedeviationInArray1675 {
    public int minimumDeviation(int[] nums) {
        // Step 1: Make all numbers even by multiplying odd numbers by 2
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        int minVal = Integer.MAX_VALUE;

        for (int num : nums) {
            if (num % 2 == 1) {
                num *= 2; // Convert odd to even
            }
            maxHeap.offer(num);
            minVal = Math.min(minVal, num);
        }

        int minDeviation = Integer.MAX_VALUE;

        // Step 2: Continuously reduce the max element and update the deviation
        while (true) {
            int maxVal = maxHeap.poll();
            minDeviation = Math.min(minDeviation, maxVal - minVal);

            // If max element is odd, stop the process
            if (maxVal % 2 == 1) {
                break;
            }

            // Otherwise, divide the max element by 2 and add it back
            maxVal /= 2;
            maxHeap.offer(maxVal);
            minVal = Math.min(minVal, maxVal);
        }

        return minDeviation;
    }

    // Testing
    public static void main(String[] args) {
        MinimisedeviationInArray1675 solution = new MinimisedeviationInArray1675();
        int[] nums = {1, 2, 3, 4};
        System.out.println("Java Test Result: " + solution.minimumDeviation(nums));  // Output should be 1
    }
}

