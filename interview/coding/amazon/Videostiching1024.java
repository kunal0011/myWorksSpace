package amazon;

import java.util.Arrays;

public class Videostiching1024 {
    public int videoStitching(int[][] clips, int T) {
        // Sort clips by start time; if two clips have the same start time, sort by end time in descending order

        Arrays.sort(clips, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            } else {
                return a[0] - b[0];
            }
        });

        // Initialize variables
        int end = 0;      // The farthest point we can reach
        int count = 0;    // The number of clips used
        int i = 0;        // Pointer to the current clip
        int n = clips.length;  // Number of clips

        while (end < T) {
            // Find the clip that starts before or at 'end' and has the farthest reach
            int farthest = end;
            while (i < n && clips[i][0] <= end) {
                farthest = Math.max(farthest, clips[i][1]);
                i++;
            }

            // If no clip can be found that extends the reach, it's impossible to cover the interval
            if (farthest == end) {
                return -1;
            }

            // Move to the farthest point
            end = farthest;
            count++;
        }

        return count;
    }

    // Testing
    public static void main(String[] args) {
        Videostiching1024 solution = new Videostiching1024();
        int[][] clips = {{0,2},{4,6},{8,10},{1,9},{1,5},{5,9}};
        int T = 10;
        System.out.println("Java Test Result: " + solution.videoStitching(clips, T));  // Output: 3
    }
}
