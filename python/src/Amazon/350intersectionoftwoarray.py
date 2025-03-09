"""
LeetCode 350: Intersection of Two Arrays II

Problem Statement:
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays, 
and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Explanation: Both arrays have two 2's, so both are included in the result.

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted as the elements can be returned in any order.

Logic:
1. Use Counter to count frequencies of elements in first array
2. Iterate through second array and check against Counter:
   - If element exists in Counter and count > 0:
     * Add to result
     * Decrease count in Counter
3. Time Complexity: O(n + m) where n, m are lengths of arrays
4. Space Complexity: O(min(n, m)) to store the counter
"""

from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a Counter (hashmap) to store the frequency of elements in nums1
        counts = Counter(nums1)
        intersection = []

        # Iterate through nums2 and collect elements that are also in nums1
        for num in nums2:
            if counts[num] > 0:  # If num is in nums1 and hasn't been fully used
                intersection.append(num)
                counts[num] -= 1  # Decrease the count since it's been used

        return intersection


def run_test_cases():
    solution = Solution()
    
    # Test case 1: Example from problem statement
    nums1_1 = [1, 2, 2, 1]
    nums2_1 = [2, 2]
    result1 = solution.intersect(nums1_1, nums2_1)
    print("Test case 1:")
    print(f"Input: nums1 = {nums1_1}, nums2 = {nums2_1}")
    print(f"Expected: [2, 2]")
    print(f"Got: {result1}")
    print(f"Pass? {sorted(result1) == sorted([2, 2])}\n")
    
    # Test case 2: Another example from problem statement
    nums1_2 = [4, 9, 5]
    nums2_2 = [9, 4, 9, 8, 4]
    result2 = solution.intersect(nums1_2, nums2_2)
    print("Test case 2:")
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Expected: [4, 9]")
    print(f"Got: {result2}")
    print(f"Pass? {sorted(result2) == sorted([4, 9])}\n")
    
    # Test case 3: No intersection
    nums1_3 = [1, 2, 3]
    nums2_3 = [4, 5, 6]
    result3 = solution.intersect(nums1_3, nums2_3)
    print("Test case 3:")
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}")
    print(f"Expected: []")
    print(f"Got: {result3}")
    print(f"Pass? {result3 == []}\n")
    
    # Test case 4: Multiple occurrences
    nums1_4 = [1, 1, 1, 2, 2]
    nums2_4 = [1, 1, 2, 2, 2]
    result4 = solution.intersect(nums1_4, nums2_4)
    print("Test case 4:")
    print(f"Input: nums1 = {nums1_4}, nums2 = {nums2_4}")
    print(f"Expected: [1, 1, 2, 2]")
    print(f"Got: {result4}")
    print(f"Pass? {sorted(result4) == sorted([1, 1, 2, 2])}\n")
    
    # Test case 5: Empty arrays
    nums1_5 = []
    nums2_5 = []
    result5 = solution.intersect(nums1_5, nums2_5)
    print("Test case 5:")
    print(f"Input: nums1 = {nums1_5}, nums2 = {nums2_5}")
    print(f"Expected: []")
    print(f"Got: {result5}")
    print(f"Pass? {result5 == []}")


if __name__ == "__main__":
    run_test_cases()
