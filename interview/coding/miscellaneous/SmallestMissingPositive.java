package miscellaneous;

public class SmallestMissingPositive {

    public static int findSmallestMissingPositive(int[] nums) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                // Swap nums[i] and nums[nums[i] - 1]
                int temp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = temp;
            }
        }

        // Find the first index where the value is not i + 1
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        // If all values are in place, return n + 1
        return n + 1;
    }

    public static void main(String[] args) {
        int[] arr1 = {3, 4, -1, 1};
        System.out.println("The smallest positive missing number is: " + findSmallestMissingPositive(arr1)); // Output: 2

        int[] arr2 = {1, 2, 0};
        System.out.println("The smallest positive missing number is: " + findSmallestMissingPositive(arr2)); // Output: 3
    }
}
