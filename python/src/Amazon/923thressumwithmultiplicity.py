"""
LeetCode 923: 3Sum With Multiplicity

Given an integer array arr, and an integer target, return the number of tuples i, j, k 
such that i < j < k and arr[i] + arr[j] + arr[k] == target.

Since the answer may be too large, return it modulo 109 + 7.

Constraints:
- 3 <= arr.length <= 3000
- 0 <= arr[i] <= 100
- 0 <= target <= 300
"""

from collections import Counter
from typing import List
from time import perf_counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = Counter(arr)
        ans = 0
        
        # Case 1: x != y != z
        for x in count:
            for y in count:
                z = target - x - y
                if z in count:
                    if x < y < z:
                        ans += count[x] * count[y] * count[z]
        
        # Case 2: x == y != z
        for x in count:
            z = target - 2*x
            if z in count and x < z:
                ans += count[x] * (count[x] - 1) * count[z] // 2
        
        # Case 3: x != y == z
        for x in count:
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if y in count and x < y:
                    ans += count[x] * count[y] * (count[y] - 1) // 2
        
        # Case 4: x == y == z
        if target % 3 == 0 and target//3 in count:
            x = target // 3
            ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
            
        return ans % MOD

def validate_input(arr: List[int], target: int) -> bool:
    """Validate input according to constraints"""
    if not 3 <= len(arr) <= 3000:
        return False
    if not all(0 <= x <= 100 for x in arr):
        return False
    if not 0 <= target <= 300:
        return False
    return True

def test_three_sum_multi():
    """Test function for 3Sum With Multiplicity"""
    test_cases = [
        ([1,1,2,2,3,3,4,4,5,5], 8, 20),
        ([1,1,1,1,1], 3, 10),
        ([2,1,3], 6, 0),
        ([1,1,2,2,2,2], 5, 12),
        ([1,2,3,3,1], 6, 2),
        ([0,0,0], 0, 1)
    ]
    
    solution = Solution()
    
    for i, (arr, target, expected) in enumerate(test_cases, 1):
        is_valid = validate_input(arr, target)
        
        start_time = perf_counter()
        result = solution.threeSumMulti(arr, target)
        end_time = perf_counter()
        
        print(f"\nTest case {i}:")
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Expected combinations: {expected}")
        print(f"Got combinations: {result}")
        print(f"Time taken: {(end_time - start_time)*1000:.3f}ms")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        count = Counter(arr)
        print("\nArray statistics:")
        print(f"Length: {len(arr)}")
        print(f"Unique elements: {len(count)}")
        print(f"Element frequencies: {dict(count)}")
        print(f"Value range: [{min(arr)}, {max(arr)}]")
        print(f"Sum range: [{3*min(arr)}, {3*max(arr)}]")

if __name__ == "__main__":
    test_three_sum_multi()
