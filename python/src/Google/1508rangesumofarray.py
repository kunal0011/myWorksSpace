"""
LeetCode 1508. Range Sum of Sorted Subarray Sums

Problem Statement:
Given the array nums consisting of n positive integers. You computed the sum of all non-empty 
continuous subarrays from the array and then sorted them in non-decreasing order, creating a new 
array of n * (n + 1) / 2 numbers. Return the sum of the numbers from index left to index right 
(indexed from 1), inclusive. Since the answer can be a huge number, return it modulo 10^9 + 7.

Time Complexity: O(n^2 * log(n^2)) due to sorting n^2 subarray sums
Space Complexity: O(n^2) to store all subarray sums
"""


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        # Logic:
        # 1. Generate all possible subarray sums:
        #    - For each starting index i
        #    - For each ending index j >= i
        #    - Calculate cumulative sum and add to list
        # 2. Sort all subarray sums
        # 3. Return sum of elements from index left to right (1-based)
        # 4. Apply modulo 10^9 + 7 to handle large numbers

        subarray_sums = []
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                subarray_sums.append(current_sum)

        subarray_sums.sort()
        return sum(subarray_sums[left-1:right]) % (10**9 + 7)


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4], 4, 1, 5),          # Expected: 13
        ([1, 2, 3, 4], 4, 3, 4),          # Expected: 6
        ([1, 2, 3, 4], 4, 1, 10),         # Expected: 50
        ([10, 20, 30, 40], 4, 1, 4)       # Expected: 100
    ]

    for i, (nums, n, left, right) in enumerate(test_cases):
        result = solution.rangeSum(nums, n, left, right)
        print(f"Test case {i + 1}:")
        print(f"Array: {nums}")
        print(f"n: {n}, left: {left}, right: {right}")
        print(f"Range sum: {result}")

        # Print all subarray sums for better understanding
        subarrays = []
        for start in range(len(nums)):
            curr_sum = 0
            for end in range(start, len(nums)):
                curr_sum += nums[end]
                subarrays.append(curr_sum)
        subarrays.sort()
        print(f"All sorted subarray sums: {subarrays}")
        print()
