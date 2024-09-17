package amazon;

public class EvenNofDigits1295 {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            // Convert the number to a string and check the length
            if (String.valueOf(num).length() % 2 == 0) {
                count++;
            }
        }
        return count;
    }

    // Test cases
    public static void main(String[] args) {
        EvenNofDigits1295 sol = new EvenNofDigits1295();

        // Test case 1
        int[] nums1 = {12, 345, 2, 6, 7896};
        int result1 = sol.findNumbers(nums1);
        assert result1 == 2 : "Test case 1 failed: " + result1;

        // Test case 2
        int[] nums2 = {555, 901, 482, 1771};
        int result2 = sol.findNumbers(nums2);
        assert result2 == 1 : "Test case 2 failed: " + result2;

        System.out.println("All test cases passed!");
    }
}
