"""
LeetCode 398: Random Pick Index

Problem Statement:
Given an integer array nums with possible duplicates, randomly output the index of a given target number. 
You can assume that the given target number must exist in the array.

Implement the Solution class:
- Solution(int[] nums) Initializes the object with the array nums.
- int pick(int target) Picks a random index i such that nums[i] == target.
Each index should be returned with equal probability.

Example:
Input:
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output: [null, 4, 0, 2]

Approaches:
1. HashMap Solution:
   - Store indices in a hash map during initialization
   - Time: O(n) space, O(1) pick
   - Better when we have more pick operations

2. Reservoir Sampling Solution:
   - No extra space needed
   - Time: O(1) space, O(n) pick
   - Better when memory is constrained
"""

import random
from collections import defaultdict
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        """
        Initialize with hash map approach - stores all indices
        Time: O(n), Space: O(n)
        """
        self.index_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.index_map[num].append(i)

    def pick(self, target: int) -> int:
        """
        Pick a random index for target using hash map
        Time: O(1), Space: O(1)
        """
        return random.choice(self.index_map[target])

class SolutionReservoir:
    def __init__(self, nums: List[int]):
        """
        Initialize with reservoir sampling approach - stores original array
        Time: O(1), Space: O(1) extra space
        """
        self.nums = nums

    def pick(self, target: int) -> int:
        """
        Pick a random index using reservoir sampling
        Time: O(n), Space: O(1)
        """
        count = 0
        result = -1
        
        # Reservoir sampling algorithm
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # Replace result with probability 1/count
                if random.randint(1, count) == 1:
                    result = i
        
        return result

def test_random_pick_index():
    """
    Test function to verify both implementations
    """
    def verify_distribution(sol, target: int, expected_indices: List[int], trials: int = 1000):
        """Helper to verify random distribution"""
        counts = defaultdict(int)
        for _ in range(trials):
            counts[sol.pick(target)] += 1
            
        # Check if all expected indices are hit
        indices_hit = set(counts.keys())
        expected_indices_set = set(expected_indices)
        assert indices_hit == expected_indices_set, \
            f"Expected indices {expected_indices_set}, got {indices_hit}"
            
        # Check if distribution is roughly uniform
        expected_freq = trials / len(expected_indices)
        tolerance = 0.2  # Allow 20% deviation
        for idx in expected_indices:
            assert abs(counts[idx] - expected_freq) < expected_freq * tolerance, \
                f"Index {idx} frequency {counts[idx]} deviates too much from expected {expected_freq}"
    
    test_cases = [
        {
            "nums": [1, 2, 3, 3, 3],
            "target": 3,
            "expected_indices": [2, 3, 4],
            "description": "Multiple occurrences of target"
        },
        {
            "nums": [1, 2, 3, 3, 3],
            "target": 1,
            "expected_indices": [0],
            "description": "Single occurrence of target"
        },
        {
            "nums": [1],
            "target": 1,
            "expected_indices": [0],
            "description": "Single element array"
        },
        {
            "nums": [1, 1, 1, 1, 1],
            "target": 1,
            "expected_indices": [0, 1, 2, 3, 4],
            "description": "All elements are target"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        target = test_case["target"]
        expected_indices = test_case["expected_indices"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Array: {nums}")
        print(f"Target: {target}")
        
        # Test HashMap solution
        print("Testing HashMap solution...")
        sol1 = Solution(nums)
        verify_distribution(sol1, target, expected_indices)
        print("✓ HashMap solution passed!")
        
        # Test Reservoir sampling solution
        print("Testing Reservoir sampling solution...")
        sol2 = SolutionReservoir(nums)
        verify_distribution(sol2, target, expected_indices)
        print("✓ Reservoir sampling solution passed!")

if __name__ == "__main__":
    test_random_pick_index()
    print("\nAll test cases passed! 🎉")
