package miscellaneous;

import java.util.LinkedList;
import java.util.Queue;

public class MinimumTimeToRotOranges {
    // Define directions (up, down, left, right)
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static int minimumTimeToRotOranges(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int freshOranges = 0;

        // Find initially rotten oranges and enqueue their coordinates
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    freshOranges++;
                }
            }
        }

        int timeElapsed = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            boolean changed = false;
            for (int i = 0; i < size; i++) {
                int[] currentOrange = queue.poll();
                for (int d = 0; d < 4; d++) {
                    int x = currentOrange[0] + dx[d];
                    int y = currentOrange[1] + dy[d];
                    if (x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] == 1) {
                        grid[x][y] = 2; // Rot the orange
                        queue.offer(new int[]{x, y});
                        freshOranges--;
                        changed = true;
                    }
                }
            }
            if (changed) {
                timeElapsed++;
            }
        }

        return freshOranges == 0 ? timeElapsed : -1; // Return timeElapsed if all oranges rotten, else -1
    }

    public static void main(String[] args) {
        int[][] grid = {
                {2, 1, 1},
                {1, 1, 0},
                {0, 1, 1}
        };

        int result = minimumTimeToRotOranges(grid);
        if (result != -1) {
            System.out.println("Minimum time required to rot all oranges: " + result);
        } else {
            System.out.println("It's not possible to rot all oranges.");
        }
    }
}
