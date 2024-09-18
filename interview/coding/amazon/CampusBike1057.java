package amazon;

import java.util.*;

public class CampusBike1057 {
    public int[] assignBikes(int[][] workers, int[][] bikes) {
        List<int[]> distances = new ArrayList<>();

        // Step 1: Calculate all distances between workers and bikes
        for (int i = 0; i < workers.length; i++) {
            for (int j = 0; j < bikes.length; j++) {
                int dist = Math.abs(workers[i][0] - bikes[j][0]) + Math.abs(workers[i][1] - bikes[j][1]);
                distances.add(new int[]{dist, i, j});
            }
        }

        // Step 2: Sort the distances by distance, then by worker index, then by bike index
        distances.sort((a, b) -> {
            if (a[0] != b[0]) {
                return a[0] - b[0]; // Compare distances
            } else if (a[1] != b[1]) {
                return a[1] - b[1]; // Compare worker index
            } else {
                return a[2] - b[2]; // Compare bike index
            }
        });

        // Step 3: Greedily assign bikes to workers
        int[] result = new int[workers.length];
        Arrays.fill(result, -1);
        boolean[] assignedBikes = new boolean[bikes.length];

        for (int[] d : distances) {
            int worker = d[1];
            int bike = d[2];
            if (result[worker] == -1 && !assignedBikes[bike]) {
                result[worker] = bike;
                assignedBikes[bike] = true;
            }
        }

        return result;
    }

    // Testing
    public static void main(String[] args) {
        CampusBike1057 solution = new CampusBike1057();
        int[][] workers = {{0,0}, {2,1}};
        int[][] bikes = {{1,2}, {3,3}};
        System.out.println("Java Test Result: " + Arrays.toString(solution.assignBikes(workers, bikes)));  // Output: [1, 0]
    }
}

