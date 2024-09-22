package amazon;

import java.util.*;

public class Findrightinterval436 {
    public int[] findRightInterval(int[][] intervals) {
        // Step 1: Create a list of (start, index) pairs
        int n = intervals.length;
        int[][] starts = new int[n][2];

        for (int i = 0; i < n; i++) {
            starts[i][0] = intervals[i][0];  // start time
            starts[i][1] = i;  // original index
        }

        // Step 2: Sort based on the start times
        Arrays.sort(starts, Comparator.comparingInt(a -> a[0]));

        // Step 3: Result array
        int[] res = new int[n];

        // Step 4: For each interval, find the right interval using binary search
        for (int i = 0; i < n; i++) {
            int end = intervals[i][1];
            int idx = binarySearch(starts, end);
            res[i] = idx;
        }

        return res;
    }

    // Binary search to find the smallest start >= end
    private int binarySearch(int[][] starts, int end) {
        int left = 0, right = starts.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (starts[mid][0] >= end) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return left < starts.length ? starts[left][1] : -1;
    }

    // Test cases
    public static void main(String[] args) {
        Findrightinterval436 sol = new Findrightinterval436();

        // Test case 1
        int[][] intervals1 = {{1, 2}};
        System.out.println(Arrays.toString(sol.findRightInterval(intervals1)));  // Expected output: [-1]

        // Test case 2
        int[][] intervals2 = {{3, 4}, {2, 3}, {1, 2}};
        System.out.println(Arrays.toString(sol.findRightInterval(intervals2)));  // Expected output: [-1, 0, 1]

        // Test case 3
        int[][] intervals3 = {{1, 4}, {2, 3}, {3, 4}};
        System.out.println(Arrays.toString(sol.findRightInterval(intervals3)));  // Expected output: [-1, 2, -1]
    }
}
