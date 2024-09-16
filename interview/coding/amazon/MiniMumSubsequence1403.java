package amazon;

import java.util.*;

public class MiniMumSubsequence1403 {
    public List<Integer> minSubsequence(int[] nums) {
        int totalSum = Arrays.stream(nums).sum();
        Integer[] numsArray = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(numsArray, Collections.reverseOrder());

        List<Integer> result = new ArrayList<>();
        int subseqSum = 0;

        for (int num : numsArray) {
            subseqSum += num;
            result.add(num);
            if (subseqSum > totalSum - subseqSum) {
                break;
            }
        }

        return result;
    }

    // Testing
    public static void main(String[] args) {
        MiniMumSubsequence1403 minimumSubSequence1403 = new MiniMumSubsequence1403();
        int[] nums = {4, 3, 10, 9, 8};
        List<Integer> result = minimumSubSequence1403.minSubsequence(nums);
        System.out.println("Java Test Result: " + result);  // Output should be [10, 9]
    }
}
