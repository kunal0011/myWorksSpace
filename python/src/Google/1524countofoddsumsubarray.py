"""
LeetCode 1524. Number of Sub-arrays With Odd Sum

Problem Statement:
Given an array of integers arr, return the number of subarrays with an odd sum.
Since the answer can be very large, return it modulo 10^9 + 7.

Time Complexity: O(n) where n is length of array
Space Complexity: O(1) as we only use constant extra space
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Logic:
        # 1. Use prefix sum technique to count subarrays with odd sum
        # 2. For each prefix sum:
        #    - If current prefix sum is even:
        #      * Number of odd sum subarrays = count of odd prefix sums before
        #    - If current prefix sum is odd:
        #      * Number of odd sum subarrays = count of even prefix sums before
        # 3. Keep track of counts of odd and even prefix sums seen so far
        # 4. Use modulo to handle large numbers

        odd_count = 0
        # Initialize with 1 for the case where prefix sum is even initially (like sum = 0)
        even_count = 1
        prefix_sum = 0
        result = 0
        MOD = 10**9 + 7

        for num in arr:
            # Update the prefix sum
            prefix_sum += num

            # Check if the prefix sum is odd or even
            if prefix_sum % 2 == 0:
                # If prefix_sum is even, add the odd_count subarrays
                result += odd_count
                even_count += 1
            else:
                # If prefix_sum is odd, add the even_count subarrays
                result += even_count
                odd_count += 1

            # Since the result can be large, take modulo MOD
            result %= MOD

        return result


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [1, 3, 5],        # Expected: 4 ([1],[1,3],[1,3,5],[3],[3,5],[5])
        [2, 4, 6],        # Expected: 0 (no subarray has odd sum)
        [1, 2, 3, 4, 5],    # Expected: 6
        [100, 100, 99, 99]  # Expected: 4
    ]

    for i, arr in enumerate(test_cases):
        result = solution.numOfSubarrays(arr)
        print(f"Test case {i + 1}:")
        print(f"Array: {arr}")
        print(f"Number of subarrays with odd sum: {result}")

        # Print all subarrays for better understanding (for small arrays)
        if len(arr) <= 5:
            print("Subarrays with odd sum:")
            for start in range(len(arr)):
                curr_sum = 0
                for end in range(start, len(arr)):
                    curr_sum += arr[end]
                    if curr_sum % 2 == 1:
                        print(f"{arr[start:end+1]} (sum={curr_sum})")
        print()
