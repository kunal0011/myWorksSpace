"""
LeetCode 523 - Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least 2 
that sums up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k.
0 is always a multiple of k.

Logic:
- Use prefix sum with modulo arithmetic and hash map to track remainders
- If we find same remainder at two different indices (at least 2 positions apart), we found a valid subarray
- Why? If (sum[i] % k) == (sum[j] % k), then sum[i:j] is divisible by k
- Edge case: k = 0 needs special handling

Time Complexity: O(n) where n is the length of nums
Space Complexity: O(min(n, k)) for the hash map of remainders
"""


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # Dictionary to store the remainder of cumulative sum and the index at which it occurred
        # Initialize with remainder 0 at index -1 for the edge case
        remainder_map = {0: -1}
        cumulative_sum = 0

        for i in range(len(nums)):
            cumulative_sum += nums[i]
            if k != 0:
                cumulative_sum %= k  # Get the remainder when cumulative_sum is divided by k

            if cumulative_sum in remainder_map:
                # Subarray must be at least size 2
                if i - remainder_map[cumulative_sum] > 1:
                    return True
            else:
                remainder_map[cumulative_sum] = i

        return False


def run_test_cases():
    solution = Solution()
    test_cases = [
        ([23, 2, 4, 6, 7], 6),      # True: [2,4] sums to 6
        # True: [23,2,6,4,7] has sum 42 which is multiple of 6
        ([23, 2, 6, 4, 7], 6),
        ([23, 2, 6, 4, 7], 13),     # False
        ([1, 2, 3], 5),           # True
        ([1, 0, 0], 2),           # True
        ([0, 0], 1),             # True
    ]

    for nums, k in test_cases:
        result = solution.checkSubarraySum(nums, k)
        print(f'Input: nums = {nums}, k = {k} -> Output: {result}')


if __name__ == "__main__":
    run_test_cases()
