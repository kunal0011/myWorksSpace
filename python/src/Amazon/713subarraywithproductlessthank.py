"""
LeetCode 713: Subarray Product Less Than K

Given an array of positive integers nums and an integer k, return the number of 
subarrays where the product of all the elements in the subarray is strictly less than k.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- 1 <= nums[i] <= 1000
- 0 <= k <= 10^6
"""

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:  # Handle edge case since all numbers are positive
            return 0
        
        count = 0
        product = 1
        left = 0
        
        # Sliding window approach
        for right in range(len(nums)):
            product *= nums[right]
            
            # Shrink window while product >= k
            while product >= k:
                product //= nums[left]
                left += 1
            
            # Add count of valid subarrays ending at right
            count += right - left + 1
            
        return count

    def numSubarrayProductLessThanK_bruteforce(self, nums: list[int], k: int) -> int:
        # Alternative implementation (slower) for verification
        if k <= 1:
            return 0
            
        count = 0
        n = len(nums)
        
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                if product < k:
                    count += 1
                else:
                    break
                    
        return count

def test_subarray_product():
    import time
    
    test_cases = [
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
        ([1, 1, 1], 2, 6),
        ([10], 100, 1),
        ([1, 1, 1, 1], 10, 10),
    ]
    
    sol = Solution()
    
    # Test optimized solution
    print("Testing optimized solution (Sliding Window):")
    start_time = time.time()
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = sol.numSubarrayProductLessThanK(nums, k)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Input: nums={nums}, k={k}")
        print(f"Expected: {expected} | Got: {result}")
    opt_time = time.time() - start_time
    
    # Test brute force solution
    print("\nTesting brute force solution:")
    start_time = time.time()
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = sol.numSubarrayProductLessThanK_bruteforce(nums, k)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Input: nums={nums}, k={k}")
        print(f"Expected: {expected} | Got: {result}")
    bf_time = time.time() - start_time
    
    print(f"\nPerformance Comparison:")
    print(f"Optimized implementation: {opt_time:.6f} seconds")
    print(f"Brute force implementation: {bf_time:.6f} seconds")
    print(f"Speed improvement: {(bf_time/opt_time):.2f}x")

if __name__ == "__main__":
    test_subarray_product()
