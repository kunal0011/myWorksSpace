"""
LeetCode 1920. Build Array from Permutation

Problem Statement:
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where 
ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

Time Complexity: O(n) where n is length of array
Space Complexity: O(n) for result array
"""

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Logic:
        # 1. Create result array of same length as input
        # 2. For each index i:
        #    - Use nums[i] as new index to get value from nums
        #    - Store nums[nums[i]] at index i in result
        # 3. Return the built array

        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [0, 2, 1, 5, 3, 4],              # Expected: [0,1,2,4,5,3]
        [5, 0, 1, 2, 3, 4],              # Expected: [4,5,0,1,2,3]
        [0, 1, 2, 3, 4, 5],              # Expected: [0,1,2,3,4,5]
        [4, 3, 2, 1, 0],                # Expected: [0,1,2,3,4]
        [2, 0, 1, 4, 3]                 # Expected: [1,2,0,3,4]
    ]

    for i, nums in enumerate(test_cases):
        result = solution.buildArray(nums)
        print(f"Test case {i + 1}:")
        print(f"Input array: {nums}")
        print(f"Output array: {result}")

        # Verify each element
        print("Verification:")
        for j in range(len(nums)):
            print(
                f"ans[{j}] = nums[nums[{j}]] = nums[{nums[j]}] = {nums[nums[j]]}")
        print()
