"""
LeetCode 493 - Reverse Pairs

Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where:
- 0 <= i < j < nums.length and
- nums[i] > 2 * nums[j]

Example:
Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
"""

from typing import List
from bisect import bisect_right

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(left: int, right: int) -> int:
            if left >= right:
                return 0
                
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            
            # Count reverse pairs
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # Merge the sorted halves
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
                    
            temp.extend(nums[i:mid + 1])
            temp.extend(nums[j:right + 1])
            nums[left:right + 1] = temp
            
            return count
            
        return merge_sort(0, len(nums) - 1) if nums else 0

def test_reverse_pairs():
    """Test function to verify the solution with multiple test cases"""
    solution = Solution()
    
    test_cases = [
        ([1,3,2,3,1], 2),
        ([2,4,3,5,1], 3),
        ([1,1,1,1,1], 0),
        ([], 0),
        ([1], 0),
        ([5,4,3,2,1], 4),
        ([1,2,3,4,5], 0),
        ([2147483647,2147483647,2147483647,2147483647,2147483647], 0)  # Edge case with max integers
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.reversePairs(nums)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"Input: {nums}")
        print(f"Expected: {expected}, Got: {result}\n")

if __name__ == "__main__":
    test_reverse_pairs()
