package amazon;

public class Champagnetower799 {
    public double champagneTower(int poured, int query_row, int query_glass) {
        // Initialize a 2D array to hold the champagne amounts, up to 100 rows
        double[][] tower = new double[101][101];
        tower[0][0] = poured;  // Pour the champagne into the top glass

        // Traverse each row and distribute the champagne
        for (int r = 0; r < query_row; r++) {
            for (int c = 0; c <= r; c++) {
                if (tower[r][c] > 1) {  // If this glass overflows
                    double excess = (tower[r][c] - 1) / 2.0;  // The excess amount to spill
                    tower[r][c] = 1;  // Cap the current glass at 1
                    tower[r + 1][c] += excess;  // Left glass in the next row
                    tower[r + 1][c + 1] += excess;  // Right glass in the next row
                }
            }
        }

        // Return the amount in the query glass, capped at 1
        return Math.min(1, tower[query_row][query_glass]);
    }

    // Test cases
    public static void main(String[] args) {
        Champagnetower799 sol = new Champagnetower799();

        // Test case 1
        int poured1 = 1;
        int query_row1 = 1;
        int query_glass1 = 1;
        System.out.println(sol.champagneTower(poured1, query_row1, query_glass1));  // Expected output: 0.0

        // Test case 2
        int poured2 = 2;
        int query_row2 = 1;
        int query_glass2 = 1;
        System.out.println(sol.champagneTower(poured2, query_row2, query_glass2));  // Expected output: 0.5

        // Test case 3
        int poured3 = 1000000000;
        int query_row3 = 99;
        int query_glass3 = 99;
        System.out.println(sol.champagneTower(poured3, query_row3, query_glass3));  // Expected output: 1.0
    }
}
