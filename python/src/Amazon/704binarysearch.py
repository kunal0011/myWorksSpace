"""
LeetCode 704: Binary Search

Given an array of integers nums which is sorted in ascending order, 
and a target integer, write a function to search target in nums. 
If target exists, return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i], target <= 10^4
- All the integers in nums are unique
- nums is sorted in ascending order
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Edge case: empty array
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Prevent integer overflow
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

def test_binary_search():
    """Test driver with comprehensive test cases"""
    solution = Solution()
    
    test_cases = [
        {
            'nums': [-1,0,3,5,9,12],
            'target': 9,
            'expected': 4,
            'description': 'Target exists in middle'
        },
        {
            'nums': [-1,0,3,5,9,12],
            'target': 2,
            'expected': -1,
            'description': 'Target does not exist'
        },
        {
            'nums': [1],
            'target': 1,
            'expected': 0,
            'description': 'Single element array, target exists'
        },
        {
            'nums': [1],
            'target': 0,
            'expected': -1,
            'description': 'Single element array, target does not exist'
        },
        {
            'nums': [-1,0,3,5,9,12],
            'target': -1,
            'expected': 0,
            'description': 'Target at first position'
        },
        {
            'nums': [-1,0,3,5,9,12],
            'target': 12,
            'expected': 5,
            'description': 'Target at last position'
        }
    ]
    
    for i, case in enumerate(test_cases, 1):
        result = solution.search(case['nums'], case['target'])
        passed = result == case['expected']
        
        print(f"\nTest case {i}: {case['description']}")
        print(f"Input array: {case['nums']}")
        print(f"Target: {case['target']}")
        print(f"Expected: {case['expected']}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if passed else '✗ Failed'}")

if __name__ == "__main__":
    test_binary_search()
