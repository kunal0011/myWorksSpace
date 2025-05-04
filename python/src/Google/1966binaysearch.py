"""
LeetCode 1966. Binary Search

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1. You must write an algorithm with O(log n) runtime complexity.

Time Complexity: O(log n) where n is length of array
Space Complexity: O(1) as we only use two pointers
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Logic:
        # 1. Use two pointers (left, right) for binary search
        # 2. While left <= right:
        #    - Calculate middle point
        #    - If target found at mid, return index
        #    - If target > mid value, search right half
        #    - If target < mid value, search left half
        # 3. If target not found, return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 3),              # Expected: 2
        ([-1, 0, 3, 5, 9, 12], 9),          # Expected: 4
        ([-1, 0, 3, 5, 9, 12], 2),          # Expected: -1
        ([1], 1),                       # Expected: 0
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8),   # Expected: 7
        ([], 5)                         # Expected: -1
    ]

    for i, (nums, target) in enumerate(test_cases):
        result = solution.search(nums, target)
        print(f"Test case {i + 1}:")
        print(f"Array: {nums}")
        print(f"Target: {target}")
        print(f"Found at index: {result}")

        # Show binary search steps
        if nums:
            left, right = 0, len(nums) - 1
            step = 1
            while left <= right:
                mid = (left + right) // 2
                print(
                    f"Step {step}: Searching between indices {left} and {right}, mid={mid} (value={nums[mid]})")
                if nums[mid] == target:
                    break
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                step += 1
        print()
