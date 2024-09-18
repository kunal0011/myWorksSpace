package amazon;

public class StoneGame877 {
    public boolean stoneGame(int[] piles) {
        // Alex always wins when both play optimally.
        return true;
    }

    // Test cases
    public static void main(String[] args) {
        StoneGame877 sol = new StoneGame877();

        // Test case 1
        int[] piles1 = {5, 3, 4, 5};
        System.out.println(sol.stoneGame(piles1));  // Expected output: True

        // Test case 2
        int[] piles2 = {3, 7, 2, 3};
        System.out.println(sol.stoneGame(piles2));  // Expected output: True
    }
}
