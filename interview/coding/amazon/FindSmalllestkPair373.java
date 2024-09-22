package amazon;

import java.util.*;

public class FindSmalllestkPair373 {
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<int[]> result = new ArrayList<>();

        // Min heap to store pairs (sum, index in nums1, index in nums2)
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        // Push the first column (nums1[i], nums2[0]) for i = 0 to min(k, len(nums1))
        for (int i = 0; i < Math.min(k, nums1.length); i++) {
            minHeap.offer(new int[] {nums1[i] + nums2[0], i, 0});
        }

        // Extract the smallest pairs from the heap up to k times
        while (k > 0 && !minHeap.isEmpty()) {
            int[] current = minHeap.poll();
            int sum = current[0], i = current[1], j = current[2];
            result.add(new int[] {nums1[i], nums2[j]});
            k--;

            // If there are more elements in nums2 for the current nums1[i], add the next pair to the heap
            if (j + 1 < nums2.length) {
                minHeap.offer(new int[] {nums1[i] + nums2[j + 1], i, j + 1});
            }
        }

        return result;
    }

    // Test cases
    public static void main(String[] args) {
        FindSmalllestkPair373 sol = new FindSmalllestkPair373();

        // Test case 1
        int[] nums1 = {1, 7, 11};
        int[] nums2 = {2, 4, 6};
        int k = 3;
        List<int[]> result = sol.kSmallestPairs(nums1, nums2, k);
        for (int[] pair : result) {
            System.out.println(Arrays.toString(pair)); // Output: [1, 2], [1, 4], [1, 6]
        }

        // Test case 2
        int[] nums1_2 = {1, 1, 2};
        int[] nums2_2 = {1, 2, 3};
        int k_2 = 2;
        result = sol.kSmallestPairs(nums1_2, nums2_2, k_2);
        for (int[] pair : result) {
            System.out.println(Arrays.toString(pair)); // Output: [1, 1], [1, 1]
        }
    }
}

