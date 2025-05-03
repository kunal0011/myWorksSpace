"""
LeetCode 398 - Random Pick Index

Given an integer array nums with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Implement the Solution class:
- Solution(int[] nums) Initializes the object with the array nums.
- int pick(int target) Picks a random index i such that nums[i] == target.
  Each index should be returned with equal probability.

Example 1:
Input:
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output: [null, 4, 0, 2]

Explanation:
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
"""

import random

class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums
    
    def pick(self, target: int) -> int:
        # Using Reservoir Sampling algorithm
        # This ensures O(1) space complexity and equal probability
        count = 0
        result = 0
        
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # Randomly select this index with probability 1/count
                if random.randint(1, count) == count:
                    result = i
        
        return result

def test_random_pick():
    # Test cases
    nums = [1, 2, 3, 3, 3]
    solution = Solution(nums)
    
    # Test picking target=3 multiple times
    print("Testing picks for target=3 (should be random among indices 2,3,4):")
    picks_3 = [solution.pick(3) for _ in range(10)]
    print(f"10 random picks for target 3: {picks_3}")
    
    # Test picking target=1 (should always be index 0)
    print("\nTesting picks for target=1 (should always be index 0):")
    picks_1 = [solution.pick(1) for _ in range(5)]
    print(f"5 picks for target 1: {picks_1}")
    assert all(p == 0 for p in picks_1), "All picks for target 1 should return index 0"
    
    # Test picking target=2 (should always be index 1)
    print("\nTesting picks for target=2 (should always be index 1):")
    picks_2 = [solution.pick(2) for _ in range(5)]
    print(f"5 picks for target 2: {picks_2}")
    assert all(p == 1 for p in picks_2), "All picks for target 2 should return index 1"
    
    print("\nAll test cases passed successfully!")

if __name__ == "__main__":
    test_random_pick()