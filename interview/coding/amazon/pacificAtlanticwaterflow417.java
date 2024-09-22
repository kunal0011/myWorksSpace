package amazon;

import java.util.*;

public class pacificAtlanticwaterflow417 {
    private int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        if (heights == null || heights.length == 0 || heights[0].length == 0) {
            return result;
        }

        int rows = heights.length;
        int cols = heights[0].length;
        boolean[][] pacific = new boolean[rows][cols];
        boolean[][] atlantic = new boolean[rows][cols];

        for (int r = 0; r < rows; r++) {
            dfs(heights, r, 0, pacific);  // Left edge
            dfs(heights, r, cols - 1, atlantic);  // Right edge
        }

        for (int c = 0; c < cols; c++) {
            dfs(heights, 0, c, pacific);  // Top edge
            dfs(heights, rows - 1, c, atlantic);  // Bottom edge
        }

        // Collect cells that can reach both oceans
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (pacific[r][c] && atlantic[r][c]) {
                    result.add(Arrays.asList(r, c));
                }
            }
        }

        return result;
    }

    private void dfs(int[][] heights, int r, int c, boolean[][] reachable) {
        reachable[r][c] = true;
        for (int[] direction : directions) {
            int newRow = r + direction[0];
            int newCol = c + direction[1];

            if (newRow >= 0 && newRow < heights.length && newCol >= 0 && newCol < heights[0].length) {
                if (!reachable[newRow][newCol] && heights[newRow][newCol] >= heights[r][c]) {
                    dfs(heights, newRow, newCol, reachable);
                }
            }
        }
    }

    // Example usage
    public static void main(String[] args) {
        pacificAtlanticwaterflow417 sol = new pacificAtlanticwaterflow417();
        int[][] heights = {
                {1, 2, 2, 3, 5},
                {3, 2, 3, 4, 4},
                {2, 4, 5, 3, 1},
                {6, 7, 1, 4, 5},
                {5, 1, 1, 2, 4}
        };
        System.out.println(sol.pacificAtlantic(heights));  // Expected output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    }
}
