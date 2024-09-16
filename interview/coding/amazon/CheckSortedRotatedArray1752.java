package amazon;

public class CheckSortedRotatedArray1752 {
    public boolean check(int[] nums) {
        int count = 0;
        int n = nums.length;

        // Count the number of "rotations" where the order breaks
        for (int i = 0; i < n; i++) {
            if (nums[i] > nums[(i + 1) % n]) {
                count++;
            }
            if (count > 1) {
                return false;
            }
        }

        return true;
    }

    // Testing the solution
    public static void main(String[] args) {
        CheckSortedRotatedArray1752 solution = new CheckSortedRotatedArray1752();

        // Test cases
        int[] nums1 = {3, 4, 5, 1, 2};
        System.out.println("Is sorted and rotated: " + solution.check(nums1));  // Expected output: True

        int[] nums2 = {2, 1, 3, 4};
        System.out.println("Is sorted and rotated: " + solution.check(nums2));  // Expected output: False

        int[] nums3 = {1, 2, 3};
        System.out.println("Is sorted and rotated: " + solution.check(nums3));  // Expected output: True
    }
}

