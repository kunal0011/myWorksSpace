"""
LeetCode 229 - Majority Element II

Problem Statement:
Given an integer array nums of size n, return all elements that appear more than ⌊n/3⌋ times.
You must solve the problem in linear time and in O(1) space.

Solution Logic:
1. Use Boyer-Moore Majority Vote algorithm modified for two candidates
2. There can be at most two elements that appear more than n/3 times
3. Two passes:
   - First pass: Find two potential candidates
   - Second pass: Verify if candidates appear > n/3 times
4. Time: O(n), Space: O(1)
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Step 1: Initialize candidates and counts
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        # Step 2: Voting process
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 3: Verification pass
        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Step 4: Determine candidates that appear more than n/3 times
        n = len(nums)
        result = []
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        return result

def test_majority_element():
    solution = Solution()
    
    # Test Case 1: Two majority elements
    nums1 = [3,2,3]
    print("Test 1: Basic case")
    print(f"Input: {nums1}")
    print(f"Output: {solution.majorityElement(nums1)}")  # Expected: [3]
    
    # Test Case 2: Single majority element
    nums2 = [1,1,1,3,3,2,2,2]
    print("\nTest 2: Multiple elements")
    print(f"Input: {nums2}")
    print(f"Output: {solution.majorityElement(nums2)}")  # Expected: [1,2]
    
    # Test Case 3: No majority elements
    nums3 = [1,2,3]
    print("\nTest 3: No majority elements")
    print(f"Input: {nums3}")
    print(f"Output: {solution.majorityElement(nums3)}")  # Expected: []
    
    # Test Case 4: All same elements
    nums4 = [2,2,2]
    print("\nTest 4: All same elements")
    print(f"Input: {nums4}")
    print(f"Output: {solution.majorityElement(nums4)}")  # Expected: [2]

if __name__ == "__main__":
    test_majority_element()
