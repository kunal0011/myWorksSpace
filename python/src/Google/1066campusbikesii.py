from functools import lru_cache


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
