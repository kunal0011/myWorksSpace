"""
LeetCode 912: Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(n log n) time complexity
and with the smallest space complexity possible.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4
"""

from typing import List
import random
from time import perf_counter

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Main sorting function that chooses best strategy based on input"""
        if len(nums) <= 16:
            return self._insertion_sort(nums[:])  # Small arrays
        elif self._is_nearly_sorted(nums):
            return self._insertion_sort(nums[:])  # Nearly sorted arrays
        else:
            return self._merge_sort(nums[:])      # General case
    
    def _merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
            
        mid = len(nums) // 2
        left = self._merge_sort(nums[:mid])
        right = self._merge_sort(nums[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def _insertion_sort(self, nums: List[int]) -> List[int]:
        """Insertion sort for small or nearly sorted arrays"""
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums
    
    def _is_nearly_sorted(self, nums: List[int], threshold: float = 0.1) -> bool:
        """Check if array is nearly sorted"""
        inversions = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                inversions += 1
                if inversions > len(nums) * threshold:
                    return False
        return True

def validate_array(nums: List[int]) -> bool:
    """Validate input array according to constraints"""
    if not 1 <= len(nums) <= 5 * 10**4:
        return False
    return all(-5 * 10**4 <= x <= 5 * 10**4 for x in nums)

def test_sort_array():
    """Test function for Sort Array"""
    test_cases = [
        ([5,2,3,1], [1,2,3,5]),
        ([5,1,1,2,0,0], [0,0,1,1,2,5]),
        (list(range(10, 0, -1)), list(range(1, 11))),
        ([3]*5, [3]*5),
        ([1], [1]),
        ([-4,0,7,4,9,-5,-1,0,-7,3], [-7,-5,-4,-1,0,0,3,4,7,9])
    ]
    
    # Add random test cases
    random_cases = [
        random.sample(range(-100, 100), 20),
        random.sample(range(-1000, 1000), 100),
        sorted(random.sample(range(-50, 50), 30))  # Nearly sorted
    ]
    
    solution = Solution()
    
    print("Testing predefined cases:")
    for i, (nums, expected) in enumerate(test_cases, 1):
        nums_copy = nums.copy()
        is_valid = validate_array(nums)
        
        start_time = perf_counter()
        result = solution.sortArray(nums_copy)
        end_time = perf_counter()
        
        print(f"\nTest case {i}:")
        print(f"Input: {nums[:20]}{'...' if len(nums) > 20 else ''}")
        print(f"Output: {result[:20]}{'...' if len(result) > 20 else ''}")
        print(f"Time taken: {(end_time - start_time)*1000:.2f}ms")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Correctly sorted: {'✓' if result == expected else '✗'}")
        
        # Additional checks
        is_sorted = all(result[i] <= result[i+1] for i in range(len(result)-1))
        same_elements = sorted(nums) == sorted(result)
        print(f"Is sorted: {'✓' if is_sorted else '✗'}")
        print(f"Contains same elements: {'✓' if same_elements else '✗'}")
    
    print("\nTesting random cases:")
    for i, nums in enumerate(random_cases, 1):
        nums_copy = nums.copy()
        expected = sorted(nums)
        
        start_time = perf_counter()
        result = solution.sortArray(nums_copy)
        end_time = perf_counter()
        
        print(f"\nRandom test {i}:")
        print(f"Array size: {len(nums)}")
        print(f"Time taken: {(end_time - start_time)*1000:.2f}ms")
        print(f"Correctly sorted: {'✓' if result == expected else '✗'}")

if __name__ == "__main__":
    test_sort_array()
