"""
LeetCode 220 - Contains Duplicate III

Problem Statement:
Given an integer array nums and two integers k and t, return true if there are two distinct indices
i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

Solution Logic:
1. Use bucket sort concept
2. Create buckets of size t+1 to group similar numbers
3. For each number:
   - Check same bucket (guaranteed difference ≤ t)
   - Check adjacent buckets
   - Remove elements outside window k
4. Time: O(n), Space: O(min(n,k))
"""

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k < 1:
            return False

        bucket = {}
        bucket_size = t + 1  # Bucket size is t + 1 to handle the range of numbers

        for i, num in enumerate(nums):
            bucket_id = num // bucket_size

            # If a number exists in the current bucket, return True
            if bucket_id in bucket:
                return True

            # Check adjacent buckets
            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= t:
                return True
            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= t:
                return True

            # Insert the number into the bucket
            bucket[bucket_id] = num

            # Remove elements outside the sliding window
            if i >= k:
                del bucket[nums[i - k] // bucket_size]

        return False

def test_contains_nearby_almost_duplicate():
    solution = Solution()
    
    # Test Case 1: Basic case
    nums1 = [1,2,3,1]
    k1, t1 = 3, 0
    print("Test 1:")
    print(f"nums={nums1}, k={k1}, t={t1}")
    print(f"Result: {solution.containsNearbyAlmostDuplicate(nums1, k1, t1)}")  # Expected: True
    
    # Test Case 2: With allowed difference
    nums2 = [1,5,9,1,5,9]
    k2, t2 = 2, 3
    print("\nTest 2:")
    print(f"nums={nums2}, k={k2}, t={t2}")
    print(f"Result: {solution.containsNearbyAlmostDuplicate(nums2, k2, t2)}")  # Expected: False
    
    # Test Case 3: Edge case
    nums3 = [1,2]
    k3, t3 = 1, 1
    print("\nTest 3:")
    print(f"nums={nums3}, k={k3}, t={t3}")
    print(f"Result: {solution.containsNearbyAlmostDuplicate(nums3, k3, t3)}")  # Expected: True
    
    # Test Case 4: Negative numbers
    nums4 = [-1,-1]
    k4, t4 = 1, 0
    print("\nTest 4:")
    print(f"nums={nums4}, k={k4}, t={t4}")
    print(f"Result: {solution.containsNearbyAlmostDuplicate(nums4, k4, t4)}")  # Expected: True

if __name__ == "__main__":
    test_contains_nearby_almost_duplicate()
