package amazon;

import java.util.*;

public class NumberOflongestIncreasingsubsequence673 {
    public int findNumberOfLIS(int[] nums) {
        if (nums.length == 0) return 0;

        int n = nums.length;
        int[] lengths = new int[n];  // lengths[i] = length of the longest subsequence ending at i
        int[] counts = new int[n];   // counts[i] = number of longest subsequences ending at i

        Arrays.fill(lengths, 1);
        Arrays.fill(counts, 1);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    if (lengths[j] + 1 > lengths[i]) {
                        lengths[i] = lengths[j] + 1;
                        counts[i] = counts[j];
                    } else if (lengths[j] + 1 == lengths[i]) {
                        counts[i] += counts[j];
                    }
                }
            }
        }

        // Find the maximum length of increasing subsequences
        int longest = 0, result = 0;
        for (int length : lengths) {
            longest = Math.max(longest, length);
        }

        // Count the number of longest subsequences
        for (int i = 0; i < n; i++) {
            if (lengths[i] == longest) {
                result += counts[i];
            }
        }

        return result;
    }

    // Test cases
    public static void main(String[] args) {
        NumberOflongestIncreasingsubsequence673 sol = new NumberOflongestIncreasingsubsequence673();

        // Test case 1
        int[] nums1 = {1, 3, 5, 4, 7};
        System.out.println(sol.findNumberOfLIS(nums1));  // Output: 2

        // Test case 2
        int[] nums2 = {2, 2, 2, 2, 2};
        System.out.println(sol.findNumberOfLIS(nums2));  // Output: 5
    }
}

