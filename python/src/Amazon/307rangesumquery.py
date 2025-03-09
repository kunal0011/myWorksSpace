"""
LeetCode 307 - Range Sum Query - Mutable (Segment Tree Implementation)

Problem Statement:
Given an integer array nums, implement a data structure that allows:
1. update(index, val): Updates element at index i to val
2. sumRange(left, right): Returns sum of elements from index left to right inclusive

Logic:
1. Use Segment Tree for efficient updates and range queries:
   - Leaf nodes store actual array values
   - Internal nodes store sum of their children
2. Tree structure:
   - Size = 2 * n where n is power of 2 ≥ input size
   - Left child = 2 * i
   - Right child = 2 * i + 1
3. Time complexity: O(log n) for both update and query
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = nums
        self.tree = [0] * (2 * n)
        # Build the segment tree
        for i in range(n):
            self.tree[n + i] = nums[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        # Update the value at index
        n = len(self.nums)
        pos = index + n
        self.tree[pos] = val
        # Update the tree
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def sumRange(self, left: int, right: int) -> int:
        # Compute the sum of the range [left, right]
        n = len(self.nums)
        left += n
        right += n
        sum_ = 0
        while left <= right:
            if left % 2 == 1:
                sum_ += self.tree[left]
                left += 1
            if right % 2 == 0:
                sum_ += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return sum_

def test_num_array():
    # Test cases
    test_cases = [
        {
            'nums': [1, 3, 5],
            'operations': [
                ('sum', (0, 2), 9),        # Test full range
                ('update', (1, 2), None),  # Update middle
                ('sum', (0, 2), 8)         # Verify update
            ]
        },
        {
            'nums': [7],
            'operations': [
                ('sum', (0, 0), 7),        # Single element sum
                ('update', (0, 4), None),  # Single element update
                ('sum', (0, 0), 4)         # Verify update
            ]
        },
        {
            'nums': [-1, 0, 1, 2],
            'operations': [
                ('sum', (1, 3), 3),        # Partial range
                ('update', (2, 5), None),  # Update with different value
                ('sum', (0, 3), 8)         # Full range after update
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
                assert result == expected, f"Sum operation failed: expected {expected}, got {result}"
                print(f"Sum range [{left},{right}] = {result}")
            else:  # update
                index, val = params
                num_array.update(index, val)
                print(f"Updated index {index} to {val}")

if __name__ == "__main__":
    test_num_array()
    print("All test cases passed!")
