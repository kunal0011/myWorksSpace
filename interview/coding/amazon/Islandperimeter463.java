package amazon;

public class Islandperimeter463 {
    public int islandPerimeter(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int perimeter = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 1) {
                    // Add 4 for the current land cell
                    perimeter += 4;

                    // Subtract 2 if there's land below
                    if (r < rows - 1 && grid[r + 1][c] == 1) {
                        perimeter -= 2;
                    }

                    // Subtract 2 if there's land to the right
                    if (c < cols - 1 && grid[r][c + 1] == 1) {
                        perimeter -= 2;
                    }
                }
            }
        }

        return perimeter;
    }

    // Test cases
    public static void main(String[] args) {
        Islandperimeter463 sol = new Islandperimeter463();

        // Test case 1
        int[][] grid1 = {
                {0, 1, 0, 0},
                {1, 1, 1, 0},
                {0, 1, 0, 0},
                {1, 1, 0, 0}
        };
        System.out.println(sol.islandPerimeter(grid1));  // Expected output: 16

        // Test case 2
        int[][] grid2 = {
                {1}
        };
        System.out.println(sol.islandPerimeter(grid2));  // Expected output: 4

        // Test case 3
        int[][] grid3 = {
                {1, 1},
                {1, 1}
        };
        System.out.println(sol.islandPerimeter(grid3));  // Expected output: 8
    }
}

