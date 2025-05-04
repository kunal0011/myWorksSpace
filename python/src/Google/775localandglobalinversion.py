"""
LeetCode 775: Global and Local Inversions

Problem Statement:
You are given an integer array nums of length n where nums is a permutation of [0, n - 1].
A global inversion is a pair of indices (i,j) where 0 <= i < j < n and nums[i] > nums[j].
A local inversion is a pair of adjacent indices (i,i+1) where 0 <= i < n-1 and nums[i] > nums[i+1].
Return true if the number of global inversions equals the number of local inversions.

Logic:
1. Key insight: Every local inversion is also a global inversion
2. For them to be equal, all global inversions must be local inversions
3. This means no element can be greater than any element that is 2 or more positions ahead
4. Therefore, each element must be at most 1 position away from its original position
5. Check if |A[i] - i| > 1 for any i. If true, return False

Time Complexity: O(n) where n is length of array
Space Complexity: O(1) since we only use constant extra space
"""

from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # Check if any element is more than 1 position away from its sorted position
        for i in range(len(nums)):
            if abs(nums[i] - i) > 1:
                return False
        return True


def test_ideal_permutation():
    solution = Solution()

    # Test case 1: Equal local and global inversions
    nums1 = [1, 0, 2]
    result1 = solution.isIdealPermutation(nums1)
    assert result1 == True, f"Test case 1 failed. Expected True, got {result1}"
    print(f"Test case 1 passed: nums={nums1}, result={result1}")

    # Test case 2: More global than local inversions
    nums2 = [1, 2, 0]
    result2 = solution.isIdealPermutation(nums2)
    assert result2 == False, f"Test case 2 failed. Expected False, got {result2}"
    print(f"\nTest case 2 passed: nums={nums2}, result={result2}")

    # Test case 3: Already sorted array
    nums3 = [0, 1, 2, 3]
    result3 = solution.isIdealPermutation(nums3)
    assert result3 == True, f"Test case 3 failed. Expected True, got {result3}"
    print(f"\nTest case 3 passed: nums={nums3}, result={result3}")

    # Test case 4: Single element array
    nums4 = [0]
    result4 = solution.isIdealPermutation(nums4)
    assert result4 == True, f"Test case 4 failed. Expected True, got {result4}"
    print(f"\nTest case 4 passed: nums={nums4}, result={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_ideal_permutation()
