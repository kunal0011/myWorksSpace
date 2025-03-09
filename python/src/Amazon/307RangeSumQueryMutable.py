"""
LeetCode 307 - Range Sum Query - Mutable

Problem Statement:
Given an integer array nums, implement a data structure that allows:
1. update(index, val): Updates element at index i to val
2. sumRange(left, right): Returns sum of elements from index left to right inclusive

The solution should handle multiple queries efficiently with frequent updates.

Logic:
1. Use Binary Indexed Tree (Fenwick Tree) for efficient updates and range queries
2. Key operations:
   - Initialize: Build BIT with cumulative sums
   - Update: Modify value and update all relevant nodes in O(log n)
   - SumRange: Calculate using prefix sums in O(log n)
3. BIT properties:
   - Each index i stores sum of values in range [i - lowbit(i) + 1, i]
   - lowbit(i) = i & (-i) gives rightmost set bit
4. Time complexity: O(log n) for both update and sum queries
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        
        # Initialize BIT
        for i in range(self.n):
            self._update_bit(i + 1, nums[i])

    def _update_bit(self, index: int, diff: int) -> None:
        while index <= self.n:
            self.bit[index] += diff
            index += index & (-index)  # Get next index in BIT

    def _get_sum(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & (-index)  # Get parent index in BIT
        return total

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self._update_bit(index + 1, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self._get_sum(right + 1) - self._get_sum(left)


def test_num_array():
    # Test cases with detailed scenarios
    test_cases = [
        {
            'nums': [1, 3, 5],
            'operations': [
                ('sum', (0, 2), 9),       # Initial sum
                ('update', (1, 2), None), # Update middle element
                ('sum', (0, 2), 8),       # Sum after update
                ('update', (0, 10), None),# Update first element
                ('sum', (0, 1), 12)       # Partial sum
            ]
        },
        {
            'nums': [-1],                 # Single element
            'operations': [
                ('sum', (0, 0), -1),
                ('update', (0, 5), None),
                ('sum', (0, 0), 5)
            ]
        },
        {
            'nums': [1, 1, 1, 1, 1],      # All same values
            'operations': [
                ('sum', (0, 4), 5),       # Full range
                ('sum', (1, 3), 3),       # Middle range
                ('update', (2, 10), None), # Update middle
                ('sum', (1, 3), 12)       # New sum
            ]
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        print(f"Initial array: {test_case['nums']}")
        num_array = NumArray(test_case['nums'].copy())
        
        for j, (op, params, expected) in enumerate(test_case['operations']):
            if op == 'sum':
                left, right = params
                result = num_array.sumRange(left, right)
                assert result == expected, f"Sum operation {j} failed: expected {expected}, got {result}"
                print(f"Sum range [{left},{right}] = {result}")
            else:  # update
                index, val = params
                original = num_array.nums[index]
                num_array.update(index, val)
                print(f"Updated index {index}: {original} -> {val}")

if __name__ == "__main__":
    test_num_array()
    print("All test cases passed!")
