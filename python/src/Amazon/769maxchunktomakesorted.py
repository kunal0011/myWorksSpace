"""
LeetCode 769: Max Chunks To Make Sorted

Given an array arr that is a permutation of [0, 1, 2, ..., n-1], we split the array into some 
number of "chunks" (partitions), and individually sort each chunk. After concatenating them, 
the result equals the sorted array.

What is the most number of chunks we could have made?

Constraints:
- n == arr.length
- 1 <= n <= 10
- 0 <= arr[i] < n
- All elements of arr are unique
- arr is a permutation of [0, 1, 2, ..., n-1]
"""

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Optimized solution using maximum tracking
        Time complexity: O(n)
        Space complexity: O(1)
        """
        chunks = 0
        curr_max = 0
        
        # If maximum value seen so far equals current position,
        # we can make a cut here for a new chunk
        for i, num in enumerate(arr):
            curr_max = max(curr_max, num)
            if curr_max == i:
                chunks += 1
                
        return chunks
    
    def maxChunksToSorted_alt(self, arr: List[int]) -> int:
        """
        Alternative solution using running sum comparison
        Time complexity: O(n)
        Space complexity: O(1)
        """
        n = len(arr)
        chunks = 0
        arr_sum = 0
        expected_sum = 0
        
        for i in range(n):
            arr_sum += arr[i]
            expected_sum += i
            if arr_sum == expected_sum:
                chunks += 1
                
        return chunks


def validate_chunks(arr: List[int], chunks: int) -> bool:
    """
    Validate if the array can be split into given number of chunks
    and sort to original array
    """
    n = len(arr)
    if chunks > n:
        return False
        
    # Try all possible chunk divisions
    def can_split(start: int, remaining_chunks: int) -> bool:
        if remaining_chunks == 0:
            return start == n
            
        for end in range(start + 1, n + 1):
            # Check if current chunk is valid
            chunk = sorted(arr[start:end])
            expected = list(range(start, end))
            if chunk == expected and can_split(end, remaining_chunks - 1):
                return True
        return False
        
    return can_split(0, chunks)


def test_max_chunks():
    """Test function for Max Chunks To Make Sorted"""
    test_cases = [
        ([4,3,2,1,0], 1),
        ([1,0,2,3,4], 4),
        ([0,1,2,3,4], 5),
        ([2,0,1], 2),
        ([1,2,0,3], 2),
        ([0], 1),
        ([0,2,1], 2)
    ]
    
    solution = Solution()
    
    for i, (arr, expected) in enumerate(test_cases, 1):
        # Test both solutions
        result1 = solution.maxChunksToSorted(arr)
        result2 = solution.maxChunksToSorted_alt(arr)
        
        print(f"\nTest case {i}:")
        print(f"Array: {arr}")
        print(f"Expected chunks: {expected}")
        print(f"Max tracking solution: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"Running sum solution: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Validate the solution
        is_valid = validate_chunks(arr, result1)
        print(f"Valid chunking: {'✓' if is_valid else '✗'}")


if __name__ == "__main__":
    test_max_chunks()
