"""
LeetCode 326 - Power of Three

Problem Statement:
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three if there exists an integer x such that n == 3^x.

Logic:
1. Use the fact that 3^19 = 1162261467 is the largest power of 3 under 2^31
2. If n is a power of 3:
   - n must be positive
   - 3^19 must be divisible by n
3. Time: O(1), Space: O(1)
   Alternative approach: Use logarithm or loop division by 3
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

def test_power_of_three():
    solution = Solution()
    
    # Test cases with explanations
    test_cases = [
        (27, True, "3^3 = 27"),
        (0, False, "0 is not a power of three"),
        (9, True, "3^2 = 9"),
        (-3, False, "Negative numbers cannot be powers of three"),
        (45, False, "45 is not a power of three"),
        (1, True, "3^0 = 1"),
        (3486784401, False, "Number larger than max int32"),
        (1594323, False, "Large non-power of three")
    ]
    
    for i, (n, expected, explanation) in enumerate(test_cases):
        result = solution.isPowerOfThree(n)
        assert result == expected, f"Test case {i + 1} failed: n={n}, expected={expected}, got={result}"
        print(f"Test case {i + 1} passed: n={n}, result={result}")
        print(f"Explanation: {explanation}\n")

if __name__ == "__main__":
    test_power_of_three()
    print("All test cases passed!")
