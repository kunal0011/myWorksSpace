"""
LeetCode 315 - Count of Smaller Numbers After Self

Problem Statement:
Given an integer array nums, return an integer array counts where counts[i] is the number
of smaller elements to the right of nums[i].

Logic:
1. Use Binary Indexed Tree (BIT) to efficiently count smaller numbers
2. Process numbers from right to left:
   - Coordinate compression to handle negative numbers
   - For each number, query BIT for count of smaller numbers
   - Update BIT with current number
3. Time: O(nlogn), Space: O(n)
"""

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def update(index: int, val: int, tree: List[int], size: int) -> None:
            index += 1
            while index <= size:
                tree[index] += val
                index += index & (-index)
        
        def query(index: int, tree: List[int]) -> int:
            index += 1
            result = 0
            while index > 0:
                result += tree[index]
                index -= index & (-index)
            return result
        
        # Coordinate compression
        sorted_nums = sorted(set(nums))
        ranks = {num: i for i, num in enumerate(sorted_nums)}
        
        n = len(ranks)
        bit = [0] * (n + 1)
        counts = []
        
        # Process numbers from right to left
        for num in reversed(nums):
            rank = ranks[num]
            counts.append(query(rank - 1, bit))
            update(rank, 1, bit, n)
        
        return counts[::-1]


def test_count_smaller():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([5,2,6,1], [2,1,1,0]),         # Standard case
        ([-1], [0]),                     # Single element
        ([1,1,1], [0,0,0]),             # All same numbers
        ([1,2,3,4], [0,0,0,0]),         # Ascending order
        ([4,3,2,1], [3,2,1,0]),         # Descending order
        ([], [])                         # Empty array
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.countSmaller(nums)
        assert result == expected, \
            f"Test case {i + 1} failed: nums={nums}, expected={expected}, got={result}"
        print(f"Test case {i + 1} passed:")
        print(f"Input array: {nums}")
        print(f"Smaller counts: {result}\n")

if __name__ == "__main__":
    test_count_smaller()
    print("All test cases passed!")
