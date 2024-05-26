package searching_sorting;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class MergeIntervals {
    public static int[][] merge(int[][] intervals) {
        if (intervals.length == 0) {
            return new int[0][];
        }

        // Sort intervals based on the starting times
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));

        // List to hold the merged intervals
        List<int[]> merged = new ArrayList<>();

        // Initialize the first interval
        int[] currentInterval = intervals[0];
        merged.add(currentInterval);

        // Iterate through the intervals
        for (int[] interval : intervals) {
            int currentEnd = currentInterval[1];
            int nextStart = interval[0];
            int nextEnd = interval[1];

            // Check if there is an overlap
            if (nextStart <= currentEnd) {
                // Merge the intervals by updating the end time
                currentInterval[1] = Math.max(currentEnd, nextEnd);
            } else {
                // No overlap, add the current interval to the list and move to the next
                currentInterval = interval;
                merged.add(currentInterval);
            }
        }

        // Convert the list to an array and return
        return merged.toArray(new int[merged.size()][]);
    }

    public static void main(String[] args) {
        int[][] intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
        int[][] mergedIntervals = merge(intervals);

        System.out.println("Merged Intervals:");
        for (int[] interval : mergedIntervals) {
            System.out.println(Arrays.toString(interval));
        }
        // Output:
        // [1, 6]
        // [8, 10]
        // [15, 18]
    }
}
