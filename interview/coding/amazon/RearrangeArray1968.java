package amazon;

 import java.util.Arrays;

public class RearrangeArray1968 {
    public int[] rearrangeArray(int[] nums) {
        Arrays.sort(nums);  // Sort the input array
        int n = nums.length;
        int[] result = new int[n];

        int left = 0;  // Pointer for the smallest elements
        int right = n - 1;  // Pointer for the largest elements

        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                result[i] = nums[left++];  // Place the smaller elements at even indices
            } else {
                result[i] = nums[right--];  // Place the larger elements at odd indices
            }
        }

        return result;
    }

    // Testing the solution
    public static void main(String[] args) {
        RearrangeArray1968 solution = new RearrangeArray1968();

        // Test case
        int[] nums = {1, 2, 3, 4, 5};
        System.out.println("Rearranged Array: " + Arrays.toString(solution.rearrangeArray(nums)));  // Expected output: [1, 5, 2, 4, 3]
    }
}
