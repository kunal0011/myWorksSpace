package amazon;

 import java.util.*;

public class NearestExit1926 {
    public int nearestExit(char[][] maze, int[] entrance) {
        int rows = maze.length, cols = maze[0].length;
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};  // right, down, left, up
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{entrance[0], entrance[1], 0});
        boolean[][] visited = new boolean[rows][cols];
        visited[entrance[0]][entrance[1]] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0], c = curr[1], steps = curr[2];

            // Check if we're at a boundary that's not the entrance
            if ((r == 0 || r == rows - 1 || c == 0 || c == cols - 1) && (r != entrance[0] || c != entrance[1])) {
                return steps;
            }

            // Explore neighbors
            for (int[] dir : directions) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc] && maze[nr][nc] == '.') {
                    visited[nr][nc] = true;
                    queue.offer(new int[]{nr, nc, steps + 1});
                }
            }
        }

        return -1;  // No exit found
    }

    // Testing the solution
    public static void main(String[] args) {
        NearestExit1926 solution = new NearestExit1926();

        // Test case
        char[][] maze = {
                {'+', '+', '.', '+'},
                {'.', '.', '.', '+'},
                {'+', '+', '+', '.'}
        };
        int[] entrance = {1, 2};
        System.out.println("Nearest Exit: " + solution.nearestExit(maze, entrance));  // Expected output: 1
    }
}
