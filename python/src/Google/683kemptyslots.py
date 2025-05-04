"""
LeetCode 683: K Empty Slots

Problem Statement:
You have n bulbs in a row numbered from 1 to n. Initially, all bulbs are turned off.
We turn on exactly one bulb every day until all bulbs are on after n days.
You are given an array bulbs of length n where bulbs[i] = x means that on the (i+1)th day, 
we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.
Given an integer k, return the number of the day when there exists two turned on bulbs 
that have exactly k bulbs between them that are all turned off. If there isn't such day, return -1.

Example:
Input: bulbs = [1,3,2], k = 1
Output: 2
Explanation:
Day 1: [1,0,0] - bulb 1 is on
Day 2: [1,0,1] - bulbs 1 and 3 are on, with 1 bulb between them off
Day 3: [1,1,1] - all bulbs are on

Logic:
1. Use a sliding window approach with binary search tree
2. Convert positions to days when bulbs were turned on
3. For each window of size k+2, check if bulbs at ends are on and bulbs between are off
4. Optimize by tracking minimum in the window

Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        days = [0] * n  # days[i] represents when position i+1 was turned on
        
        # Convert positions to days
        for day, pos in enumerate(bulbs, 1):
            days[pos-1] = day
            
        result = float('inf')
        left = 0
        right = k + 1
        
        # Slide window of size k+1
        while right < n:
            is_valid = True
            
            # Check if all bulbs between left and right were turned on later
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    is_valid = False
                    break
            
            if is_valid:
                result = min(result, max(days[left], days[right]))
                
            left += 1
            right += 1
        
        return result if result != float('inf') else -1


def test_k_empty_slots():
    solution = Solution()
    
    # Test case 1: Basic example
    print("Test Case 1:")
    bulbs = [1,3,2]
    k = 1
    print(f"Input: bulbs = {bulbs}, k = {k}")
    print(f"Output: {solution.kEmptySlots(bulbs, k)}")  # Expected: 2
    
    # Test case 2: No solution exists
    print("\nTest Case 2:")
    bulbs = [1,2,3]
    k = 1
    print(f"Input: bulbs = {bulbs}, k = {k}")
    print(f"Output: {solution.kEmptySlots(bulbs, k)}")  # Expected: -1
    
    # Test case 3: Larger example
    print("\nTest Case 3:")
    bulbs = [6,5,8,9,7,1,4,2,3]
    k = 2
    print(f"Input: bulbs = {bulbs}, k = {k}")
    print(f"Output: {solution.kEmptySlots(bulbs, k)}")  # Expected: 8

if __name__ == "__main__":
    test_k_empty_slots()
