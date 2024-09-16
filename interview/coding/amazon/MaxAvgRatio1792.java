package amazon;

import java.util.PriorityQueue;

public class MaxAvgRatio1792 {
    double improvement(int passed, int total) {
        return (double)(passed + 1) / (total + 1) - (double)passed / total;
    }
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        // Helper function to calculate the improvement in pass ratio


        // Create a max heap with a custom comparator
        PriorityQueue<double[]> maxHeap = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));

        // Add each class to the heap
        for (int[] c : classes) {
            maxHeap.offer(new double[]{improvement(c[0], c[1]), c[0], c[1]});
        }

        // Add extra students to the classes with the greatest improvement
        for (int i = 0; i < extraStudents; i++) {
            double[] top = maxHeap.poll();
            int passed = (int)top[1];
            int total = (int)top[2];
            passed++;
            total++;
            maxHeap.offer(new double[]{improvement(passed, total), passed, total});
        }

        // Calculate the final average pass ratio
        double totalAvg = 0;
        for (double[] entry : maxHeap) {
            totalAvg += entry[1] / entry[2];
        }

        return totalAvg / classes.length;
    }

    // Testing the solution
    public static void main(String[] args) {
        MaxAvgRatio1792 solution = new MaxAvgRatio1792();

        // Test case
        int[][] classes = {{1, 2}, {3, 5}, {2, 2}};
        int extraStudents = 2;
        System.out.println("Max average pass ratio: " + solution.maxAverageRatio(classes, extraStudents));  // Expected output: ~0.78333
    }
}
