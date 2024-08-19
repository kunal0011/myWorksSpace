from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points):
        count = 0

        # Iterate over each point to calculate distances to all other points
        for i in points:
            distance_map = defaultdict(int)

            for j in points:
                if i == j:
                    continue
                # Calculate squared distance between points i and j
                dist = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                distance_map[dist] += 1

            # For each distance, calculate the number of boomerangs
            for val in distance_map.values():
                count += val * (val - 1)  # k * (k-1) boomerangs

        return count
