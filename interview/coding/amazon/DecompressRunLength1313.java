package amazon;

import java.util.ArrayList;
import java.util.List;

public class DecompressRunLength1313 {
    public int[] decompressRLElist(int[] nums) {
        List<Integer> resultList = new ArrayList<>();

        // Step through the array in pairs of (frequency, value)
        for (int i = 0; i < nums.length; i += 2) {
            int freq = nums[i];
            int val = nums[i + 1];
            // Append `val` `freq` times to the result list
            for (int j = 0; j < freq; j++) {
                resultList.add(val);
            }
        }

        // Convert the result list to an array
        int[] result = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            result[i] = resultList.get(i);
        }
        return result;
    }

    // Testing
    public static void main(String[] args) {
        DecompressRunLength1313 solution = new DecompressRunLength1313();
        int[] nums = {1, 2, 3, 4};
        int[] result = solution.decompressRLElist(nums);
        System.out.println("Java Test Result: " + java.util.Arrays.toString(result));  // Output: [2, 4, 4, 4]
    }
}
