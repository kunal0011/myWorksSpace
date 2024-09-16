package amazon;

public class MinimumSumStep1413 {
public int minStartValue(int[] nums) {
        int currentSum = 0;
        int minSum = 0;

        for (int num : nums) {
        currentSum += num;
        minSum = Math.min(minSum, currentSum);
        }

        return -minSum + 1;
        }

// Testing
public static void main(String[] args) {
        MinimumSumStep1413 minimumSumStep1413 = new MinimumSumStep1413();
        int[] nums = {1, -2, -3};
        System.out.println("Java Test Result: " + minimumSumStep1413.minStartValue(nums));  // Output should be 5
        }
        }

