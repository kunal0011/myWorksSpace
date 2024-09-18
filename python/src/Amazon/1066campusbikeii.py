from functools import lru_cache
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        # Function to calculate the Manhattan distance
        def manhattan(worker, bike):
            return abs(workers[worker][0] - bikes[bike][0]) + abs(workers[worker][1] - bikes[bike][1])

        # Use memoization to store the minimum cost for each worker and bike assignment
        @lru_cache(None)
        def dp(worker, used_bikes):
            # Base case: If all workers are assigned bikes
            if worker == len(workers):
                return 0

            # Try assigning this worker to all available bikes and calculate the minimum cost
            min_cost = float('inf')
            for bike in range(len(bikes)):
                # If this bike has not been used yet
                if not used_bikes & (1 << bike):
                    cost = manhattan(worker, bike) + \
                        dp(worker + 1, used_bikes | (1 << bike))
                    min_cost = min(min_cost, cost)

            return min_cost

        # Start with the first worker and no bikes assigned (used_bikes = 0)
        return dp(0, 0)


# Testing
solution = Solution()
workers = [[0, 0], [2, 1]]
bikes = [[1, 2], [3, 3]]
print("Python Test Result:", solution.assignBikes(workers, bikes))  # Output: 6
