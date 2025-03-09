"""
LeetCode 349: Intersection of Two Arrays

Problem Statement:
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Explanation: The common element that appears in both arrays is 2, and we only include it once.

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted as a valid answer.

Logic:
1. Use set data structure to remove duplicates and for O(1) lookup
2. Convert both arrays to sets to get unique elements
3. Use set intersection operator (&) to find common elements
4. Convert result back to list
5. Time Complexity: O(n + m) where n, m are lengths of input arrays
6. Space Complexity: O(min(n, m)) to store the intersection
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets
        set1 = set(nums1)
        set2 = set(nums2)

        # Find the intersection of both sets
        intersection = set1 & set2

        # Convert the result to a list
        return list(intersection)


def run_test_cases():
    solution = Solution()
    
    # Test case 1: Example from problem statement
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    result1 = solution.intersection(nums1_1, nums2_1)
    print("Test case 1:")
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Expected: [2]")
    print(f"Got: {result1}")
    print(f"Pass? {sorted(result1) == [2]}\n")
    
    # Test case 2: Another example from problem statement
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    result2 = solution.intersection(nums1_2, nums2_2)
    print("Test case 2:")
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Expected: [4, 9] (in any order)")
    print(f"Got: {result2}")
    print(f"Pass? {sorted(result2) == sorted([4, 9])}\n")
    
    # Test case 3: No intersection
    nums1_3 = [1, 2, 3]
    nums2_3 = [4, 5, 6]
    result3 = solution.intersection(nums1_3, nums2_3)
    print("Test case 3:")
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}")
    print(f"Expected: []")
    print(f"Got: {result3}")
    print(f"Pass? {result3 == []}\n")
    
    # Test case 4: All elements intersect
    nums1_4 = [1, 2, 3]
    nums2_4 = [3, 2, 1]
    result4 = solution.intersection(nums1_4, nums2_4)
    print("Test case 4:")
    print(f"Input: nums1 = {nums1_4}, nums2 = {nums2_4}")
    print(f"Expected: [1, 2, 3] (in any order)")
    print(f"Got: {result4}")
    print(f"Pass? {sorted(result4) == sorted([1, 2, 3])}\n")
    
    # Test case 5: Empty arrays
    nums1_5 = []
    nums2_5 = []
    result5 = solution.intersection(nums1_5, nums2_5)
    print("Test case 5:")
    print(f"Input: nums1 = {nums1_5}, nums2 = {nums2_5}")
    print(f"Expected: []")
    print(f"Got: {result5}")
    print(f"Pass? {result5 == []}")


if __name__ == "__main__":
    run_test_cases()
