package amazon;

import java.util.*;

public class CreateTargetArray1389 {
    public int[] createTargetArray(int[] nums, int[] index) {
        List<Integer> target = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            target.add(index[i], nums[i]);
        }

        // Convert the list to an array
        return target.stream().mapToInt(Integer::intValue).toArray();
    }

    // Testing
    public static void main(String[] args) {
        CreateTargetArray1389 solution = new CreateTargetArray1389();
        int[] nums = {0, 1, 2, 3, 4};
        int[] index = {0, 1, 2, 2, 1};
        int[] result = solution.createTargetArray(nums, index);
        System.out.print("Java Test Result: ");
        for (int num : result) {
            System.out.print(num + " ");
        }
        // Output should be [0, 4, 1, 3, 2]
    }
}
