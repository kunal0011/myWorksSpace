"""
LeetCode 852: Peak Index in Mountain Array

An array arr is a mountain if the following properties hold:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] < ... < arr[i-1] < arr[i]
  - arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Constraints:
- 3 <= arr.length <= 10^5
- 0 <= arr[i] <= 10^6
- arr is guaranteed to be a mountain array
"""

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 1, len(arr) - 2  # Peak can't be at ends
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                left = mid + 1  # Peak is to the right
            else:
                right = mid - 1  # Peak is to the left
                
        return left  # Will always find peak due to problem constraints

def validate_mountain_array(arr: List[int]) -> bool:
    """Validate if array is a mountain array and meets constraints"""
    if not 3 <= len(arr) <= 10**5:
        return False
    if not all(0 <= x <= 10**6 for x in arr):
        return False
        
    # Check if it's actually a mountain
    peak = max(range(1, len(arr)-1), key=lambda i: arr[i])
    return all(arr[i-1] < arr[i] for i in range(1, peak+1)) and \
           all(arr[i] > arr[i+1] for i in range(peak, len(arr)-1))

def test_peak_index():
    """Test function for Peak Index in Mountain Array"""
    test_cases = [
        ([0,2,4,7,6,3,1], 3),
        ([0,1,0], 1),
        ([0,10,5,2], 1),
        ([3,4,5,1], 2),
        ([24,69,100,99,79,78,67,36,26,19], 2)
    ]
    
    solution = Solution()
    
    for i, (arr, expected) in enumerate(test_cases, 1):
        is_valid = validate_mountain_array(arr)
        result = solution.peakIndexInMountainArray(arr)
        
        print(f"\nTest case {i}:")
        print(f"Array: {arr}")
        print(f"Expected peak index: {expected}")
        print(f"Found peak index: {result}")
        print(f"Peak value: {arr[result]}")
        print(f"Valid mountain array: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Visualize the mountain
        max_height = max(arr)
        mountain = ""
        for j, height in enumerate(arr):
            spaces = " " * (j * 2)
            stars = "*" * height
            marker = "^" if j == result else " "
            mountain += f"{spaces}{stars} {marker}\n"
        print("\nMountain visualization:")
        print(mountain)

if __name__ == "__main__":
    test_peak_index()
