package amazon;

import java.util.HashSet;

public class Faircandyswap888 {
    public int[] fairCandySwap(int[] AliceSizes, int[] BobSizes) {
        int sumA = 0, sumB = 0;
        for (int x : AliceSizes) sumA += x;
        for (int x : BobSizes) sumB += x;

        int delta = (sumA - sumB) / 2;
        HashSet<Integer> setB = new HashSet<>();
        for (int y : BobSizes) setB.add(y);

        for (int x : AliceSizes) {
            if (setB.contains(x - delta)) {
                return new int[]{x, x - delta};
            }
        }
        return new int[]{};
    }

    // Test case
    public static void main(String[] args) {
        Faircandyswap888 solution = new Faircandyswap888();
        int[] AliceSizes = {1, 1};
        int[] BobSizes = {2, 2};
        int[] result = solution.fairCandySwap(AliceSizes, BobSizes);
        System.out.println("Fair swap: [" + result[0] + ", " + result[1] + "]");
    }
}
