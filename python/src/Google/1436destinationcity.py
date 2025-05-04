"""
LeetCode 1436. Destination City

Problem Statement:
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore exactly one destination city exists.

Time Complexity: O(n) where n is the number of paths
Space Complexity: O(n) to store the set of starting cities
"""

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Logic:
        # 1. Create a set of all starting cities (cities that have outgoing paths)
        # 2. Iterate through all paths and find the destination city that is not in the starting cities set
        # 3. This city will be the final destination as it has no outgoing paths

        # Set of cities that are starting points
        start_cities = set(cityA for cityA, cityB in paths)

        # Iterate over destination cities and find the one that is not a start city
        for cityA, cityB in paths:
            if cityB not in start_cities:
                return cityB


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
        [["B", "C"], ["D", "B"], ["C", "A"]],
        [["A", "Z"]]
    ]

    for i, test_case in enumerate(test_cases):
        result = solution.destCity(test_case)
        print(f"Test case {i + 1}:")
        print(f"Paths: {test_case}")
        print(f"Destination city: {result}")
        print()
