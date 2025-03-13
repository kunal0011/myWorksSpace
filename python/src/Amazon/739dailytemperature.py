"""
LeetCode 739: Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait 
after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stack to store indices
        
        # Handle edge cases
        if n <= 1:
            return result
            
        # Process each temperature
        for curr_day, curr_temp in enumerate(temperatures):
            # Check if current temperature is warmer than previous days
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                result[prev_day] = curr_day - prev_day
            stack.append(curr_day)
            
        return result


def test_daily_temperatures():
    """Test function with comprehensive test cases"""
    solution = Solution()
    test_cases = [
        # Basic test cases
        (
            [73,74,75,71,69,72,76,73],
            [1,1,4,2,1,1,0,0]
        ),
        (
            [30,40,50,60],
            [1,1,1,0]
        ),
        (
            [30,60,90],
            [1,1,0]
        ),
        
        # Edge cases
        (
            [1],
            [0]
        ),
        (
            [],
            []
        ),
        
        # Special cases
        (
            [90,80,70,60],  # Decreasing temperatures
            [0,0,0,0]
        ),
        (
            [60,60,60,60],  # Same temperatures
            [0,0,0,0]
        ),
        (
            [30,29,28,27,26,25,24,23,22,21,20],  # Strictly decreasing
            [0,0,0,0,0,0,0,0,0,0,0]
        ),
        (
            [20,21,22,23,24,25],  # Strictly increasing
            [1,1,1,1,1,0]
        )
    ]

    for i, (temps, expected) in enumerate(test_cases, 1):
        result = solution.dailyTemperatures(temps)
        success = result == expected
        print(f"\nTest case {i}:")
        print(f"Input: {temps}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if success else '✗ Failed'}")


if __name__ == "__main__":
    test_daily_temperatures()
