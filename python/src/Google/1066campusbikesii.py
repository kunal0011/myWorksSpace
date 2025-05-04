"""
LeetCode 1066: Campus Bikes II

Problem Statement:
On a campus represented as a 2D grid, there are n workers and m bikes, with n <= m.
Each worker and bike is a 2D coordinate on this grid. We assign one unique bike to each worker
such that the sum of the Manhattan distances between each worker and their assigned bike is minimized.
Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

Logic:
1. Use Dynamic Programming with Backtracking:
   - State: (worker_index, bike_mask) where bike_mask tracks assigned bikes
   - For each worker, try all available bikes
   - Use bit manipulation to track bike assignments efficiently
2. Optimization using memoization (@lru_cache)
3. Manhattan distance = |x1-x2| + |y1-y2|
4. Base case: when all workers are assigned bikes

Time Complexity: O(n * 2^m) where n = workers, m = bikes
Space Complexity: O(n * 2^m) for memoization
"""

from functools import lru_cache
from typing import List


class Solution:
    def assignBikes(self, workers, bikes) -> int:
        @lru_cache(None)
        def dfs(worker_index, bike_mask):
            if worker_index == len(workers):
                return 0

            min_distance = float('inf')
            for bike_index in range(len(bikes)):
                if not (bike_mask & (1 << bike_index)):  # Check if bike is not yet assigned
                    new_bike_mask = bike_mask | (1 << bike_index)
                    distance = abs(workers[worker_index][0] - bikes[bike_index][0]) + abs(
                        workers[worker_index][1] - bikes[bike_index][1])
                    min_distance = min(
                        min_distance, distance + dfs(worker_index + 1, new_bike_mask))

            return min_distance

        return dfs(0, 0)


def test_assign_bikes():
    solution = Solution()

    # Test case 1: Basic case
    workers1 = [[0, 0], [2, 1]]
    bikes1 = [[1, 2], [3, 3]]
    result1 = solution.assignBikes(workers1, bikes1)
    assert result1 == 6, f"Test case 1 failed. Expected 6, got {result1}"
    print(f"Test case 1 passed: Total distance = {result1}")

    # Test case 2: Multiple possible assignments
    workers2 = [[0, 0], [1, 1], [2, 0]]
    bikes2 = [[1, 0], [2, 2], [2, 1]]
    result2 = solution.assignBikes(workers2, bikes2)
    assert result2 == 4, f"Test case 2 failed. Expected 4, got {result2}"
    print(f"\nTest case 2 passed: Total distance = {result2}")

    # Test case 3: Single worker and bike
    workers3 = [[0, 0]]
    bikes3 = [[1, 1]]
    result3 = solution.assignBikes(workers3, bikes3)
    assert result3 == 2, f"Test case 3 failed. Expected 2, got {result3}"
    print(f"\nTest case 3 passed: Total distance = {result3}")

    # Test case 4: Workers and bikes at same positions
    workers4 = [[0, 0], [1, 1]]
    bikes4 = [[0, 0], [1, 1]]
    result4 = solution.assignBikes(workers4, bikes4)
    assert result4 == 0, f"Test case 4 failed. Expected 0, got {result4}"
    print(f"\nTest case 4 passed: Total distance = {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_assign_bikes()
