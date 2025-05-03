"""
LeetCode 315 - Count of Smaller Numbers After Self

Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
- To the right of 5: 2 and 1 are smaller (2)
- To the right of 2: 1 is smaller (1)
- To the right of 6: 1 is smaller (1)
- To the right of 1: no smaller elements (0)

Example 2:
Input: nums = [-1]
Output: [0]

Example 3:
Input: nums = [-1,-1]
Output: [0,0]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

from typing import List


class BinaryIndexedTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    
    def update(self, index, val):
        while index <= self.size:
            self.tree[index] += val
            index += index & (-index)
    
    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Handle empty input
        if not nums:
            return []
        
        # Discretization: map numbers to their ranks
        sorted_nums = sorted(set(nums))
        ranks = {num: i + 1 for i, num in enumerate(sorted_nums)}
        
        # Initialize BIT with size equal to number of unique elements
        bit = BinaryIndexedTree(len(ranks))
        
        # Process numbers from right to left
        result = []
        for num in reversed(nums):
            rank = ranks[num]
            result.append(bit.query(rank - 1))  # Count smaller numbers
            bit.update(rank, 1)  # Add current number
        
        return result[::-1]  # Reverse to get correct order


def test_count_smaller():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([5,2,6,1], [2,1,1,0]),
        ([-1], [0]),
        ([-1,-1], [0,0]),
        ([1,2,3,4], [0,0,0,0]),
        ([4,3,2,1], [3,2,1,0]),
        ([3,2,2,1], [2,1,1,0])
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.countSmaller(nums)
        assert result == expected, f"Test case {i + 1} failed: got {result}, expected {expected}"
        print(f"Test case {i + 1} passed! Input: {nums}, Output: {result}")


if __name__ == "__main__":
    test_count_smaller()