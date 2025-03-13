"""
LeetCode 698: Partition to K Equal Sum Subsets

Given an integer array nums and an integer k, return true if it is possible to divide this array 
into k non-empty subsets whose sums are all equal.
"""

from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Early pruning
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        n = len(nums)
        
        # Sort in descending order for optimization
        nums.sort(reverse=True)
        
        # If any number is greater than target sum, impossible to partition
        if nums[0] > target:
            return False
            
        # Used as cache key
        used = 0
        cache = {}
        
        def backtrack(index: int, count: int, curr_sum: int) -> bool:
            nonlocal used
            
            # All k subsets found
            if count == k:
                return True
                
            # Current subset sum equals target, start new subset
            if curr_sum == target:
                return backtrack(0, count + 1, 0)
                
            # Check cache
            if (used, count, curr_sum) in cache:
                return cache[(used, count, curr_sum)]
                
            # Try including remaining numbers
            for i in range(index, n):
                # Skip if number already used or adding it exceeds target
                if (used >> i) & 1 or curr_sum + nums[i] > target:
                    continue
                    
                # Skip duplicates at same level
                if i > 0 and nums[i] == nums[i-1] and not ((used >> (i-1)) & 1):
                    continue
                    
                # Include current number
                used |= (1 << i)
                if backtrack(i + 1, count, curr_sum + nums[i]):
                    return True
                used ^= (1 << i)
                
            cache[(used, count, curr_sum)] = False
            return False
            
        return backtrack(0, 0, 0)

def test_partition_k_subsets():
    test_cases = [
        ([4,3,2,3,5,2,1], 4, True),
        ([1,2,3,4], 3, False),
        ([2,2,2,2,3,4,5], 4, False),
        ([1,1,1,1,2,2,2,2], 4, True),
    ]
    
    solution = Solution()
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = solution.canPartitionKSubsets(nums, k)
        print(f"Test case {i}:")
        print(f"nums = {nums}, k = {k}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}\n")

if __name__ == "__main__":
    test_partition_k_subsets()
