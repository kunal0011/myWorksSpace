from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []

        # Step 1: Calculate all distances between workers and bikes
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                distances.append((dist, i, j))

        # Step 2: Sort the distances by distance, then by worker index, then by bike index
        distances.sort()

        # Step 3: Greedily assign bikes to workers
        result = [-1] * len(workers)
        assigned_bikes = set()

        for dist, worker, bike in distances:
            if result[worker] == -1 and bike not in assigned_bikes:
                result[worker] = bike
                assigned_bikes.add(bike)

        return result


# Testing
solution = Solution()
workers = [[0, 0], [2, 1]]
bikes = [[1, 2], [3, 3]]
print("Python Test Result:", solution.assignBikes(
    workers, bikes))  # Output: [1, 0]
