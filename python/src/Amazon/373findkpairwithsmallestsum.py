"""
LeetCode 373: Find K Pairs with Smallest Sums
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1,v1),(u2,v2),...,(uk,vk) with the smallest sums.

Time Complexity: O(k * log(k))
Space Complexity: O(k)
"""

import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        # Optimization: We don't need to process more than k pairs
        m, n = len(nums1), len(nums2)
        k = min(k, m * n)  # Optimize k to not exceed total possible pairs
        
        # Min heap to store tuples (sum, index in nums1, index in nums2)
        min_heap = []
        result = []
        
        # Use a set to keep track of visited pairs to avoid duplicates
        visited = set()
        
        # Start with the smallest possible sum (first elements of both arrays)
        heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        
        while k > 0 and min_heap:
            curr_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1
            
            # Try next element in nums2
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            
            # Try next element in nums1
            if j == 0 and i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
        
        return result


def run_test_case(nums1: List[int], nums2: List[int], k: int, expected: List[List[int]]) -> None:
    """Helper function to run test cases and verify results."""
    sol = Solution()
    result = sol.kSmallestPairs(nums1, nums2, k)
    print(f"\nInput:")
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"k = {k}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print(f"Test {'PASSED' if result == expected else 'FAILED'}")


# Test cases
if __name__ == "__main__":
    # Test case 1: Basic case
    run_test_case(
        nums1=[1, 7, 11],
        nums2=[2, 4, 6],
        k=3,
        expected=[[1, 2], [1, 4], [1, 6]]
    )

    # Test case 2: Duplicate values
    run_test_case(
        nums1=[1, 1, 2],
        nums2=[1, 2, 3],
        k=2,
        expected=[[1, 1], [1, 1]]
    )

    # Test case 3: Small arrays
    run_test_case(
        nums1=[1, 2],
        nums2=[3],
        k=3,
        expected=[[1, 3], [2, 3]]
    )

    # Test case 4: k larger than possible pairs
    run_test_case(
        nums1=[1, 2],
        nums2=[3, 4],
        k=10,
        expected=[[1, 3], [1, 4], [2, 3], [2, 4]]
    )

    # Test case 5: Empty arrays
    run_test_case(
        nums1=[],
        nums2=[3, 4],
        k=2,
        expected=[]
    )
