package amazon;

import java.util.*;

public class ThirdMaximum414 {
    public int thirdMax(int[] nums) {
        Set<Integer> distinctNums = new HashSet<>();
        for (int num : nums) {
            distinctNums.add(num);
        }

        List<Integer> sortedNums = new ArrayList<>(distinctNums);
        Collections.sort(sortedNums, Collections.reverseOrder());

        if (sortedNums.size() < 3) {
            return sortedNums.get(0);
        }

        return sortedNums.get(2);  // Return the third largest
    }

    public static void main(String[] args) {
        ThirdMaximum414 sol = new ThirdMaximum414();
        System.out.println(sol.thirdMax(new int[]{3, 2, 1}));  // Expected output: 1
        System.out.println(sol.thirdMax(new int[]{1, 2}));      // Expected output: 2
        System.out.println(sol.thirdMax(new int[]{2, 2, 3, 1})); // Expected output: 1
    }
}

