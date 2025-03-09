"""
LeetCode 231 - Power of Two

Problem Statement:
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two if there exists an integer x such that n == 2^x.

Solution Logic:
1. Bit Manipulation Approach:
   - Powers of 2 have exactly one '1' bit in their binary representation
   - n & (n-1) removes the rightmost 1-bit
   - For powers of 2, this operation should give 0
2. Edge case: handle n <= 0
3. Time: O(1), Space: O(1)

Alternative Solutions:
1. Recursive: return n > 0 and (n == 1 or (n % 2 == 0 and isPowerOfTwo(n // 2)))
2. Iterative: Repeatedly divide by 2 and check remainder
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

def test_power_of_two():
    solution = Solution()
    
    # Test Case 1: Power of 2
    n1 = 16
    print("Test 1: Power of 2")
    print(f"Input: {n1}")
    print(f"Output: {solution.isPowerOfTwo(n1)}")  # Expected: True
    
    # Test Case 2: Not power of 2
    n2 = 3
    print("\nTest 2: Not power of 2")
    print(f"Input: {n2}")
    print(f"Output: {solution.isPowerOfTwo(n2)}")  # Expected: False
    
    # Test Case 3: Negative number
    n3 = -16
    print("\nTest 3: Negative number")
    print(f"Input: {n3}")
    print(f"Output: {solution.isPowerOfTwo(n3)}")  # Expected: False
    
    # Test Case 4: Edge case
    n4 = 1
    print("\nTest 4: Edge case (2^0)")
    print(f"Input: {n4}")
    print(f"Output: {solution.isPowerOfTwo(n4)}")  # Expected: True

if __name__ == "__main__":
    test_power_of_two()
