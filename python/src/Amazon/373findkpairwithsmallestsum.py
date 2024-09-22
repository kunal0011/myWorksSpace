import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        # Check for empty arrays
        if not nums1 or not nums2:
            return []

        # Min heap to store tuples (sum, index in nums1, index in nums2)
        min_heap = []

        # Push the first row (nums1[i], nums2[0]) for i = 0 to min(k, len(nums1))
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        result = []

        # Extract the smallest pairs from the heap up to k times
        while k > 0 and min_heap:
            # Pop the smallest element from the heap
            sum_val, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            # If there are more elements in nums2 for the current nums1[i], add the next pair to the heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    # Output: [[1, 2], [1, 4], [1, 6]]
    print(sol.kSmallestPairs(nums1, nums2, k))

    # Test case 2
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    print(sol.kSmallestPairs(nums1, nums2, k))  # Output: [[1, 1], [1, 1]]

    # Test case 3
    nums1 = [1, 2]
    nums2 = [3]
    k = 3
    print(sol.kSmallestPairs(nums1, nums2, k))  # Output: [[1, 3], [2, 3]]
