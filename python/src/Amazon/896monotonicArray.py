"""
LeetCode 896: Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, and false otherwise.

Constraints:
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
"""

class Solution:
    def isMonotonic(self, A: list[int]) -> bool:
        if len(A) <= 2:
            return True
            
        # Determine direction from first inequality
        direction = 0  # 0: undefined, 1: increasing, -1: decreasing
        
        for i in range(1, len(A)):
            if A[i] > A[i-1]:  # increasing
                if direction == -1:
                    return False
                direction = 1
            elif A[i] < A[i-1]:  # decreasing
                if direction == 1:
                    return False
                direction = -1
                
        return True

def validate_array(arr: list[int]) -> bool:
    """Validate input array constraints"""
    if not 1 <= len(arr) <= 10**5:
        return False
    if any(not -10**5 <= x <= 10**5 for x in arr):
        return False
    return True

def test_monotonic_array():
    """Test function for Monotonic Array"""
    test_cases = [
        ([1,2,2,3], True),
        ([6,5,4,4], True),
        ([1,3,2], False),
        ([1,1,1], True),
        ([1], True),
        ([1,2,4,5], True),
        ([5,4,3,2,1], True),
        ([1,1,0,3], False),
        ([-1,-5,-10,-11], True),
        ([1,2,2,3,2], False)
    ]
    
    solution = Solution()
    
    for i, (arr, expected) in enumerate(test_cases, 1):
        is_valid = validate_array(arr)
        result = solution.isMonotonic(arr)
        
        print(f"\nTest case {i}:")
        print(f"Array: {arr}")
        print(f"Expected: {expected}")
        print(f"Result: {result} {'✓' if result == expected else '✗'}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        if result:
            print(f"Type: {'Increasing' if arr[-1] >= arr[0] else 'Decreasing'} monotonic")

if __name__ == "__main__":
    test_monotonic_array()
