from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Set of cities that are starting points
        start_cities = set(cityA for cityA, cityB in paths)

        # Iterate over destination cities and find the one that is not a start city
        for cityA, cityB in paths:
            if cityB not in start_cities:
                return cityB
