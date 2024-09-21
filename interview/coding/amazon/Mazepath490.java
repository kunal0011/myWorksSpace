package amazon;

import java.util.*;

public class Mazepath490 {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        int rows = maze.length, cols = maze[0].length;
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        Queue<int[]> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.offer(start);
        visited.add(Arrays.toString(start));

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0], y = current[1];

            // If we reach the destination
            if (x == destination[0] && y == destination[1]) {
                return true;
            }

            for (int[] dir : directions) {
                int nx = x, ny = y;
                // Roll the ball in the current direction until hitting a wall
                while (nx + dir[0] >= 0 && nx + dir[0] < rows &&
                        ny + dir[1] >= 0 && ny + dir[1] < cols &&
                        maze[nx + dir[0]][ny + dir[1]] == 0) {
                    nx += dir[0];
                    ny += dir[1];
                }

                // If the new position is not visited, add it to the queue
                String pos = nx + "," + ny;
                if (!visited.contains(pos)) {
                    visited.add(pos);
                    queue.offer(new int[]{nx, ny});
                }
            }
        }

        return false;
    }

    // Test cases
    public static void main(String[] args) {
        Mazepath490 sol = new Mazepath490();

        // Test case 1
        int[][] maze1 = {
                {0, 0, 0},
                {0, 1, 0},
                {0, 0, 0}
        };
        int[] start1 = {0, 0};
        int[] destination1 = {0, 2};
        System.out.println(sol.hasPath(maze1, start1, destination1));  // Expected output: true

        // Test case 2
        int[][] maze2 = {
                {0, 0, 0},
                {0, 1, 0},
                {0, 0, 0}
        };
        int[] start2 = {0, 0};
        int[] destination2 = {1, 2};
        System.out.println(sol.hasPath(maze2, start2, destination2));  // Expected output: false
    }
}
