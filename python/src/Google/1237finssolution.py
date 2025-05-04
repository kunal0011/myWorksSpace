"""
LeetCode 1237: Find Positive Integer Solution for a Given Equation

Problem Statement:
Given a callable function f(x, y) with a hidden implementation that takes two positive integers x and y
as input and returns an integer f(x, y), find all pairs of positive integers (x, y) such that
f(x, y) == z for a given z, where 1 ≤ x, y ≤ 1000.

Logic:
1. Use two pointers approach (similar to search in sorted 2D matrix)
2. Start with x = 1 and y = 1000:
   - If f(x,y) == z: Found a solution, increment x and decrement y
   - If f(x,y) < z: Need larger value, increment x
   - If f(x,y) > z: Need smaller value, decrement y
3. Continue until x > 1000 or y < 1

Time Complexity: O(x + y) where x,y ≤ 1000
Space Complexity: O(k) where k is number of solutions
"""

# This is a custom class to simulate the hidden function


class CustomFunction:
    def f(self, x, y):
        return x + y  # Example implementation


class Solution:
    def findSolution(self, customFunction, z):
        results = []
        x, y = 1, 1000

        while x <= 1000 and y > 0:
            result = customFunction.f(x, y)
            if result == z:
                results.append([x, y])
                x += 1
                y -= 1
            elif result < z:
                x += 1
            else:
                y -= 1

        return results


def test_find_solution():
    solution = Solution()

    # Test case 1: f(x,y) = x + y, z = 5
    custom_func1 = CustomFunction()
    result1 = solution.findSolution(custom_func1, 5)
    expected1 = [[1, 4], [2, 3], [3, 2], [4, 1]]
    assert sorted(result1) == sorted(
        expected1), f"Test case 1 failed. Expected {expected1}, got {result1}"
    print(f"Test case 1 passed: z = 5, solutions = {result1}")

    # Test case 2: f(x,y) = x + y, z = 1
    custom_func2 = CustomFunction()
    result2 = solution.findSolution(custom_func2, 1)
    assert result2 == [], f"Test case 2 failed. Expected [], got {result2}"
    print(f"\nTest case 2 passed: z = 1, solutions = {result2}")

    # Test case 3: f(x,y) = x + y, z = 2000
    custom_func3 = CustomFunction()
    result3 = solution.findSolution(custom_func3, 2000)
    assert result3 == [], f"Test case 3 failed. Expected [], got {result3}"
    print(f"\nTest case 3 passed: z = 2000, solutions = {result3}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_find_solution()
