"""
LeetCode 760: Find Anagram Mappings

Problem Statement:
You are given two integer arrays nums1 and nums2 where nums2 is an anagram of nums1. Both arrays may contain duplicates.
Return an index mapping array mapping from nums1 to nums2 where mapping[i] = j means the ith element in nums1 appears in nums2 at index j.
If there are multiple answers, return any of them.

Logic:
1. Create a hashmap to store value-to-index mappings from nums2
   - For duplicates, store the last occurrence (or any occurrence)
2. For each number in nums1, look up its index in the hashmap
3. Return the array of mapped indices

Time Complexity: O(n) where n is the length of the arrays
Space Complexity: O(n) for storing the hashmap
"""

from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a hashmap to store the value and its corresponding index in nums2
        index_map = {value: index for index, value in enumerate(nums2)}

        # Create the result list by mapping each value in nums1 to its index in nums2
        result = [index_map[num] for num in nums1]

        return result


def test_anagram_mappings():
    solution = Solution()

    # Test case 1: Basic case
    nums1_1 = [12, 28, 46, 32, 50]
    nums2_1 = [50, 12, 32, 46, 28]
    result1 = solution.anagramMappings(nums1_1, nums2_1)
    print(
        f"Test case 1:\nNums1: {nums1_1}\nNums2: {nums2_1}\nMapping: {result1}")
    # Verify that the mapping is correct
    assert all(nums1_1[i] == nums2_1[result1[i]] for i in range(len(nums1_1)))

    # Test case 2: With duplicates
    nums1_2 = [84, 46, 46, 84]
    nums2_2 = [84, 84, 46, 46]
    result2 = solution.anagramMappings(nums1_2, nums2_2)
    print(
        f"\nTest case 2:\nNums1: {nums1_2}\nNums2: {nums2_2}\nMapping: {result2}")
    assert all(nums1_2[i] == nums2_2[result2[i]] for i in range(len(nums1_2)))

    # Test case 3: Single element
    nums1_3 = [1]
    nums2_3 = [1]
    result3 = solution.anagramMappings(nums1_3, nums2_3)
    print(
        f"\nTest case 3:\nNums1: {nums1_3}\nNums2: {nums2_3}\nMapping: {result3}")
    assert all(nums1_3[i] == nums2_3[result3[i]] for i in range(len(nums1_3)))

    print("\nAll test cases passed!")
