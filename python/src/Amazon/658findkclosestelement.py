"""
LeetCode 658: Find K Closest Elements

Problem Statement:
Given a sorted integer array arr, two integers k and x, return the k closest integers 
to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b
"""

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Binary search solution to find the start of k closest elements
        Time complexity: O(log(n-k)) for binary search
        Space complexity: O(1)
        """
        if len(arr) == k:
            return arr
            
        left, right = 0, len(arr) - k
        
        # Binary search to find the left bound of the window
        while left < right:
            mid = left + (right - left) // 2
            
            # Compare the boundaries of current window
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
                
        return arr[left:left + k]
    
    def findClosestElements_sliding(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Alternative sliding window solution for comparison
        Time complexity: O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        
        while right - left >= k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
                
        return arr[left:right + 1]

def test_solution():
    """Test driver with various test cases"""
    solution = Solution()
    
    test_cases = [
        {
            "arr": [1,2,3,4,5], 
            "k": 4, 
            "x": 3,
            "description": "Basic case",
            "expected": [1,2,3,4]
        },
        {
            "arr": [1,2,3,4,5],
            "k": 4,
            "x": -1,
            "description": "Target less than all elements",
            "expected": [1,2,3,4]
        },
        {
            "arr": [1,1,1,10,10,10],
            "k": 1,
            "x": 9,
            "description": "Duplicate elements",
            "expected": [10]
        },
        {
            "arr": [-2,-1,1,2,3,4,5],
            "k": 7,
            "x": 3,
            "description": "Negative numbers",
            "expected": [-2,-1,1,2,3,4,5]
        }
    ]
    
    for tc in test_cases:
        print(f"\nTest Case: {tc['description']}")
        print(f"Array: {tc['arr']}")
        print(f"k: {tc['k']}, x: {tc['x']}")
        
        # Test both implementations
        result1 = solution.findClosestElements(tc['arr'], tc['k'], tc['x'])
        result2 = solution.findClosestElements_sliding(tc['arr'], tc['k'], tc['x'])
        
        print(f"Expected: {tc['expected']}")
        print(f"Binary Search Result: {result1}")
        print(f"Sliding Window Result: {result2}")
        print(f"Binary Search {'✓' if result1 == tc['expected'] else '✗'}")
        print(f"Sliding Window {'✓' if result2 == tc['expected'] else '✗'}")
        print("-" * 50)

if __name__ == "__main__":
    test_solution()
