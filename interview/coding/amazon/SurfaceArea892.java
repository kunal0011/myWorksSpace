package amazon;

public class SurfaceArea892 {
    public int surfaceArea(int[][] grid) {
        int n = grid.length;
        int surfaceArea = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    // Add top and bottom surfaces
                    surfaceArea += 2;
                    // Add the four side surfaces
                    surfaceArea += grid[i][j] * 4;

                    // Subtract areas hidden by adjacent cubes
                    if (i > 0) {
                        surfaceArea -= Math.min(grid[i][j], grid[i - 1][j]) * 2;
                    }
                    if (j > 0) {
                        surfaceArea -= Math.min(grid[i][j], grid[i][j - 1]) * 2;
                    }
                }
            }
        }

        return surfaceArea;
    }

    public static void main(String[] args) {
        SurfaceArea892 sol = new SurfaceArea892();
        int[][] grid = {{1, 2}, {3, 4}};
        System.out.println(sol.surfaceArea(grid));  // Output: 34
    }
}
