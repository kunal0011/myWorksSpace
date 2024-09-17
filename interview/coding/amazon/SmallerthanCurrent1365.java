package amazon;

import java.util.Arrays;
import java.util.HashMap;

public class SmallerthanCurrent1365 {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        // Step 1: Create a sorted copy of the array
        int[] sortedNums = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sortedNums);

        // Step 2: Create a hashmap to store the number of elements smaller than each number
        HashMap<Integer, Integer> numToCount = new HashMap<>();

        // Step 3: Populate the hashmap with the index of each element in the sorted array
        for (int i = 0; i < sortedNums.length; i++) {
            if (!numToCount.containsKey(sortedNums[i])) {
                numToCount.put(sortedNums[i], i);
            }
        }

        // Step 4: Create the result array
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = numToCount.get(nums[i]);
        }

        return result;
    }

    // Testing
    public static void main(String[] args) {
        SmallerthanCurrent1365 solution = new SmallerthanCurrent1365();
        int[] nums = {8, 1, 2, 2, 3};
        System.out.println("Java Test Result: " + Arrays.toString(solution.smallerNumbersThanCurrent(nums)));  // Output: [4, 0, 1, 1, 3]
    }
}
