"""
LeetCode 321 - Create Maximum Number

Problem Statement:
You are given two integer arrays nums1 and nums2 of length m and n respectively.
Create the maximum number of length k <= m + n from digits of the two arrays.
The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.

Example:
Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]
"""

from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_max_array(nums: List[int], k: int) -> List[int]:
            stack = []
            drop = len(nums) - k  # number of digits we can drop
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            result = []
            while arr1 or arr2:
                if arr1 > arr2:
                    result.append(arr1[0])
                    arr1 = arr1[1:]
                else:
                    result.append(arr2[0])
                    arr2 = arr2[1:]
            return result

        n1, n2 = len(nums1), len(nums2)
        max_result = []
        
        # Try all possible combinations of selecting i numbers from nums1 
        # and k-i numbers from nums2
        for i in range(k + 1):
            if i <= n1 and k - i <= n2:  # Check if selection is possible
                candidate = merge(
                    get_max_array(nums1, i),
                    get_max_array(nums2, k - i)
                )
                max_result = max(max_result, candidate)
        
        return max_result

def run_tests():
    solution = Solution()
    
    test_cases = [
        (
            [3,4,6,5],
            [9,1,2,5,8,3],
            5,
            [9,8,6,5,3]
        ),
        (
            [6,7],
            [6,0,4],
            5,
            [6,7,6,0,4]
        ),
        (
            [3,9],
            [8,9],
            3,
            [9,8,9]
        ),
        (
            [2,5,6,4,4,0],
            [7,3,8,0,6,5,7,6,2],
            15,
            [7,3,8,2,5,6,4,4,0,0,6,5,7,6,2]
        )
    ]
    
    for i, (nums1, nums2, k, expected) in enumerate(test_cases, 1):
        result = solution.maxNumber(nums1, nums2, k)
        print(f"\nTest case {i}:")
        print(f"nums1: {nums1}")
        print(f"nums2: {nums2}")
        print(f"k: {k}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")

if __name__ == "__main__":
    run_tests()