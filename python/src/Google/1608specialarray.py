"""
LeetCode 1608. Special Array With X Elements Greater Than or Equal X

Problem Statement:
You are given an array nums of non-negative integers. Let x be any integer such that x is
greater than or equal to x elements in nums. Return the smallest such integer x.
If no such integer exists, return -1.

Time Complexity: O(nlogn) due to sorting
Space Complexity: O(1) as we sort in-place
"""


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        # Logic:
        # 1. Sort array in descending order to optimize checking
        # 2. For each possible value x from 1 to len(nums):
        #    - Check if exactly x numbers are >= x
        #    - This is true if nums[x-1] >= x (at least x numbers are >= x)
        #      and (x = n or nums[x] < x) (not more than x numbers are >= x)
        # 3. Return -1 if no such x exists

        nums.sort(reverse=True)
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= i and (i == len(nums) or nums[i] < i):
                return i
        return -1


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [3, 5],              # Expected: 2 (both 3 and 5 are >= 2)
        [0, 0],              # Expected: -1 (no valid x exists)
        [0, 4, 3, 0, 4],        # Expected: 3 (exactly 3 elements >= 3)
        [3, 6, 7, 7, 0],        # Expected: 4 (exactly 4 elements >= 4)
        [1, 2, 3, 4, 5]         # Expected: 3 (exactly 3 elements >= 3)
    ]

    for i, nums in enumerate(test_cases):
        result = solution.specialArray(nums)
        print(f"Test case {i + 1}:")
        print(f"Input array: {nums}")
        print(f"Special integer x: {result}")
        if result != -1:
            count = sum(1 for num in nums if num >= result)
            print(f"Verification: {count} numbers are >= {result}")
        else:
            print("No special integer exists")
        print()
