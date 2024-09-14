package amazon;

import java.util.ArrayList;
import java.util.List;

public class PartitionArrayWithGivenPivot2161 {
    public int[] pivotArray(int[] nums, int pivot) {
        List<Integer> lessThanPivot = new ArrayList<>();
        List<Integer> equalToPivot = new ArrayList<>();
        List<Integer> greaterThanPivot = new ArrayList<>();

        // Partition the array into three categories
        for (int num : nums) {
            if (num < pivot) {
                lessThanPivot.add(num);
            } else if (num == pivot) {
                equalToPivot.add(num);
            } else {
                greaterThanPivot.add(num);
            }
        }

        // Fill the original array with the concatenated result
        int index = 0;
        for (int num : lessThanPivot) {
            nums[index++] = num;
        }
        for (int num : equalToPivot) {
            nums[index++] = num;
        }
        for (int num : greaterThanPivot) {
            nums[index++] = num;
        }

        return nums;
    }
}
