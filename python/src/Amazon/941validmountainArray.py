"""
LeetCode 941: Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
  * arr[0] < arr[1] < ... < arr[i-1] < arr[i]
  * arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^4
"""

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
            
        i = 0
        
        # Walk up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
            
        # Peak can't be first or last element
        if i == 0 or i == n - 1:
            return False
            
        # Walk down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
            
        return i == n - 1

def validate_array(arr: List[int]) -> bool:
    """Validate array according to constraints"""
    if not 1 <= len(arr) <= 10**4:
        return False
    return all(0 <= x <= 10**4 for x in arr)

def visualize_mountain(arr: List[int], peak_index: int = -1) -> str:
    """Create visual representation of the array as mountain"""
    max_height = max(arr)
    scale = 30 // max_height
    result = []
    
    for i, height in enumerate(arr):
        spaces = " " * i
        stars = "*" * (height * scale)
        marker = "^" if i == peak_index else " "
        result.append(f"{spaces}{stars} {marker} ({height})")
    
    return "\n".join(result)

def test_valid_mountain():
    """Test function for Valid Mountain Array"""
    test_cases = [
        ([2,1], False),
        ([3,5,5], False),
        ([0,3,2,1], True),
        ([0,1,2,3,4,5], False),
        ([5,4,3,2,1], False),
        ([0,2,3,4,5,2,1], True),
        ([0,2,3,3,5,2,1], False)
    ]
    
    solution = Solution()
    
    for i, (arr, expected) in enumerate(test_cases, 1):
        is_valid = validate_array(arr)
        result = solution.validMountainArray(arr)
        
        # Find peak if it exists
        peak_index = -1
        if len(arr) >= 3:
            for j in range(1, len(arr)-1):
                if arr[j-1] < arr[j] > arr[j+1]:
                    peak_index = j
                    break
        
        print(f"\nTest case {i}:")
        print(f"Array: {arr}")
        print("\nVisualization:")
        print(visualize_mountain(arr, peak_index))
        print(f"\nIs mountain array: {'✓' if result else '✗'}")
        print(f"Expected: {'✓' if expected else '✗'}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional analysis
        if len(arr) >= 3:
            print("\nArray properties:")
            print(f"Length: {len(arr)}")
            print(f"Peak index: {peak_index if peak_index != -1 else 'None'}")
            print(f"Peak value: {arr[peak_index] if peak_index != -1 else 'None'}")
            print(f"Strictly increasing up to peak: {'✓' if peak_index != -1 and all(arr[j] < arr[j+1] for j in range(peak_index)) else '✗'}")
            print(f"Strictly decreasing after peak: {'✓' if peak_index != -1 and all(arr[j] > arr[j+1] for j in range(peak_index, len(arr)-1)) else '✗'}")

if __name__ == "__main__":
    test_valid_mountain()
