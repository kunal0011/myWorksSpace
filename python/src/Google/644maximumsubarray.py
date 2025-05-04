"""
LeetCode 644 - Maximum Average Subarray II

Problem Statement:
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is greater than or equal to k that has the maximum average value.
Return this value rounded to 10^-5 decimal places.

Logic:
1. Use Binary Search approach on answer space
   - The maximum average must lie between min and max values in array
   - For each potential average value, check if it's possible to find a subarray with higher average
2. For each guess value 'mid':
   - Convert problem to finding a subarray sum > 0 by subtracting mid from each element
   - Use prefix sum technique to efficiently check if such subarray exists
3. Binary search continues until we reach desired precision

Time Complexity: O(n * log((max-min)/ε)) where ε is the error tolerance
Space Complexity: O(n)

Key Optimizations:
1. Use binary search on result space instead of checking all possible subarrays
2. Use cumulative sum for efficient subarray calculations
3. Early termination in check function when possible
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def check(average: float) -> bool:
            # Check if there exists a subarray with average > mid
            prefix_sum = [0] * (len(nums) + 1)
            min_sum = float('inf')

            # Calculate prefix sum with average subtracted
            for i in range(len(nums)):
                prefix_sum[i + 1] = prefix_sum[i] + nums[i] - average

                if i >= k - 1:
                    min_sum = min(min_sum, prefix_sum[i - k + 1])
                    if prefix_sum[i + 1] - min_sum >= 0:
                        return True
            return False

        left = min(nums)
        right = max(nums)
        epsilon = 1e-5

        # Binary search on the average value
        while right - left > epsilon:
            mid = (left + right) / 2
            if check(mid):
                left = mid
            else:
                right = mid

        return left


def test_maximum_average_subarray():
    solution = Solution()

    # Test Case 1: Basic case
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    print(f"\nTest Case 1:")
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {solution.findMaxAverage(nums1, k1)}")
    print(f"Expected: 12.75")

    # Test Case 2: Minimum length case
    nums2 = [5]
    k2 = 1
    print(f"\nTest Case 2:")
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {solution.findMaxAverage(nums2, k2)}")
    print(f"Expected: 5.0")

    # Test Case 3: Negative numbers
    nums3 = [-1, -2, -3, -4, -5]
    k3 = 2
    print(f"\nTest Case 3:")
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {solution.findMaxAverage(nums3, k3)}")
    print(f"Expected: -1.5")

    # Test Case 4: Longer array
    nums4 = [4, 2, 1, 3, 3, 5, 6, 7, 8]
    k4 = 3
    print(f"\nTest Case 4:")
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output: {solution.findMaxAverage(nums4, k4)}")
    print(f"Expected: 7.0")


if __name__ == "__main__":
    test_maximum_average_subarray()
