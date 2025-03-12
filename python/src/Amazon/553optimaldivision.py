"""
LeetCode 553 - Optimal Division

You are given an array of positive integers nums. You need to find the maximum value of the expression:
nums[0] / nums[1] / nums[2] / ... / nums[n-1]
by adding parentheses to the expression.

Note:
1. The length of nums is in range [1, 10].
2. Each number in nums is a positive integer in range [1, 1000].
3. You can add any number of parentheses at any position of the expression.
4. The test cases are generated to ensure that the output values fit in a 32-bit floating-point number.

Example 1:
Input: nums = [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 1000/(10/2) = 1000/5 = 200
However:
1000/100/10/2 = 1000/100/10/2 = 10/10/2 = 1/2 = 0.5
1000/(100/(10/2)) = 1000/50 = 20

Example 2:
Input: nums = [2,3,4]
Output: "2/(3/4)"
Explanation: 2/(3/4) = 8/3 = 2.667

Example 3:
Input: nums = [2]
Output: "2"
Explanation: There is no way to add parentheses to change the value.
"""

from typing import List
from fractions import Fraction

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        """
        Optimized solution with mathematical insight
        Time Complexity: O(1) - only need to format the string
        Space Complexity: O(1) - output string size is bounded
        """
        if not nums:
            return ""
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
            
        # Key insight: To maximize a/b/c/d, we want a divided by the minimum possible value
        # The minimum value will be achieved by b/c/d without any parentheses
        # So optimal solution is always: a/(b/c/d/...)
        result = str(nums[0]) + "/(" + str(nums[1])
        for i in range(2, len(nums)):
            result += "/" + str(nums[i])
        result += ")"
        
        return result

    def evaluate_expression(self, nums: List[int]) -> float:
        """
        Helper method to evaluate the division expression
        Uses Fraction to maintain precision
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return float(nums[0])
            
        # For optimal division: a/(b/c/d/...)
        numerator = Fraction(nums[0])
        denominator = Fraction(nums[1])
        
        for i in range(2, len(nums)):
            denominator /= Fraction(nums[i])
            
        return float(numerator / denominator)


def test_optimal_division():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([1000,100,10,2], "1000/(100/10/2)"),
        ([2,3,4], "2/(3/4)"),
        ([2], "2"),
        
        # Edge cases
        ([1,2], "1/2"),
        ([7], "7"),
        
        # Additional test cases
        ([5,2,1], "5/(2/1)"),
        ([10,5,2,1], "10/(5/2/1)"),
        ([3,2,1,4], "3/(2/1/4)"),
    ]
    
    print("Running tests for Optimal Division...\n")
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.optimalDivision(nums)
        value = solution.evaluate_expression(nums)
        
        print(f"Test Case {i}:")
        print(f"Input: nums = {nums}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Evaluated Value: {value:.3f}")
        
        if result == expected:
            print("✅ Test case passed!")
        else:
            print("❌ Test case failed!")
            
        # Print mathematical verification
        print(f"Mathematical verification:")
        print(f"- Expression: {result}")
        print(f"- Value: {value:.3f}\n")


if __name__ == "__main__":
    test_optimal_division()
