"""
LeetCode 213 - House Robber II

Problem Statement:
You are a professional robber planning to rob houses arranged in a circle. Each house has a certain 
amount of money stashed. Adjacent houses have security systems connected, and you can't rob adjacent 
houses. Given an integer array nums representing the amount of money in each house, return the maximum 
amount of money you can rob without alerting the police.

Solution Logic:
1. Houses are in circle (first and last are adjacent)
2. Break into two subproblems:
   - Rob houses from 0 to n-2 (exclude last)
   - Rob houses from 1 to n-1 (exclude first)
3. Use dynamic programming for each subarray:
   - rob1 = previous max without current house
   - rob2 = current max including current house
4. Time: O(n), Space: O(1)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            rob1, rob2 = 0, 0
            for amount in houses:
                new_rob = max(rob2, rob1 + amount)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        if len(nums) == 1:
            return nums[0]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

def test_house_robber():
    solution = Solution()
    
    # Test Case 1: Simple circular arrangement
    nums1 = [2,3,2]
    print("Test Case 1:")
    print(f"Houses: {nums1}")
    print(f"Maximum money: {solution.rob(nums1)}")  # Expected: 3
    
    # Test Case 2: Four houses
    nums2 = [1,2,3,1]
    print("\nTest Case 2:")
    print(f"Houses: {nums2}")
    print(f"Maximum money: {solution.rob(nums2)}")  # Expected: 4
    
    # Test Case 3: Single house
    nums3 = [1]
    print("\nTest Case 3:")
    print(f"Houses: {nums3}")
    print(f"Maximum money: {solution.rob(nums3)}")  # Expected: 1
    
    # Test Case 4: Large values
    nums4 = [200,3,140,20,10]
    print("\nTest Case 4:")
    print(f"Houses: {nums4}")
    print(f"Maximum money: {solution.rob(nums4)}")  # Expected: 340

if __name__ == "__main__":
    test_house_robber()
