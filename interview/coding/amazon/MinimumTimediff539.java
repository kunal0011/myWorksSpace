package amazon;

import java.util.Arrays;
import java.util.List;

public class MinimumTimediff539 {
    public int findMinDifference(List<String> timePoints) {
        // Helper function to convert time "HH:MM" to total minutes
        int[] minutes = new int[timePoints.size()];

        for (int i = 0; i < timePoints.size(); i++) {
            String[] time = timePoints.get(i).split(":");
            int hours = Integer.parseInt(time[0]);
            int mins = Integer.parseInt(time[1]);
            minutes[i] = hours * 60 + mins;
        }

        // Sort the time points in minutes
        Arrays.sort(minutes);

        // Initialize the minimum difference to a large value
        int minDiff = Integer.MAX_VALUE;

        // Calculate the difference between consecutive time points
        for (int i = 1; i < minutes.length; i++) {
            minDiff = Math.min(minDiff, minutes[i] - minutes[i - 1]);
        }

        // Compare the circular difference between the first and last time point
        minDiff = Math.min(minDiff, 1440 - (minutes[minutes.length - 1] - minutes[0]));

        return minDiff;
    }

    // Test cases
    public static void main(String[] args) {
        MinimumTimediff539 sol = new MinimumTimediff539();

        // Test case 1
        List<String> timePoints1 = Arrays.asList("23:59", "00:00");
        System.out.println(sol.findMinDifference(timePoints1));  // Expected output: 1

        // Test case 2
        List<String> timePoints2 = Arrays.asList("12:01", "23:59", "00:00");
        System.out.println(sol.findMinDifference(timePoints2));  // Expected output: 1
    }
}

