"""
LeetCode 454 - 4Sum II

Problem Statement:
-----------------
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the 
number of tuples (i, j, k, l) such that:
- 0 <= i, j, k, l < n
- nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Key Points:
----------
1. Need to find count of quadruplets that sum to 0
2. Arrays can contain both positive and negative integers
3. Can use elements at same index multiple times
4. No need to avoid duplicates in result count
5. Uses hash map to optimize from O(n⁴) to O(n²)

Examples:
--------
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation: Two tuples (i,j,k,l) that sum to 0:
1. (0,0,0,1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1,1,0,0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
Explanation: The tuple (0,0,0,0) sums to 0.

Constraints:
-----------
* n == nums1.length == nums2.length == nums3.length == nums4.length
* 1 <= n <= 200
* -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
"""

from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], 
                    nums3: List[int], nums4: List[int]) -> int:
        """
        Find number of quadruplets (one from each array) that sum to 0.
        
        Algorithm:
        1. Split the problem into two parts for optimization
        2. Create hash map of sums from first two arrays
        3. Check for complementary sums from last two arrays
        4. Use defaultdict to handle missing keys automatically
        
        Time Complexity: O(n²) where n is length of input arrays
        Space Complexity: O(n²) to store sums in hash map
        """
        count = 0
        sum_map = defaultdict(int)  # Maps sum -> frequency

        # First part: compute all possible sums of nums1 and nums2
        for a in nums1:
            for b in nums2:
                sum_map[a + b] += 1

        # Second part: check if -(c+d) exists in hash map
        for c in nums3:
            for d in nums4:
                target = -(c + d)  # Looking for complement to make total sum 0
                count += sum_map[target]  # Add frequency of complementary sum

        return count


def test_four_sum_count():
    """
    Test driver for 4Sum II problem
    """
    test_cases = [
        (
            [1,2], [-2,-1], [-1,2], [0,2],
            2  # Basic case with multiple solutions
        ),
        (
            [0], [0], [0], [0],
            1  # Single element arrays
        ),
        (
            [1], [1], [1], [1],
            0  # No solutions possible
        ),
        (
            [-1,-1], [-1,-1], [1,1], [1,1],
            16  # All combinations work
        ),
        (
            [1,1,-1,-1], [1,-1,1,-1], [1,1,-1,-1], [1,-1,1,-1],
            256  # Complex case with many solutions
        ),
        (
            [], [], [], [],
            0  # Empty arrays
        ),
        (
            [1,2,3], [-2,-1,0], [-1,2,3], [0,2,4],
            8  # Larger arrays
        ),
        (
            [-1000000000], [1000000000], [1000000000], [-1000000000],
            1  # Large numbers
        )
    ]
    
    solution = Solution()
    
    for i, (nums1, nums2, nums3, nums4, expected) in enumerate(test_cases, 1):
        result = solution.fourSumCount(nums1, nums2, nums3, nums4)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"nums1: {nums1}")
        print(f"nums2: {nums2}")
        print(f"nums3: {nums3}")
        print(f"nums4: {nums4}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_four_sum_count()
