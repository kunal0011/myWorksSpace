"""
LeetCode 1854. Maximum Population Year

Problem Statement:
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years
of the ith person. The population of some year x is the number of people alive during that year. The ith person is
counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Return the earliest year with
the maximum population.

Time Complexity: O(n + y) where n is number of logs and y is year range
Space Complexity: O(y) where y is the range of years
"""

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Logic:
        # 1. Use line sweep algorithm with prefix sum
        # 2. For each birth year, increment count by 1
        # 3. For each death year, decrement count by 1
        # 4. Scan through years to find earliest year with max population

        # Determine the minimum and maximum years based on the logs
        min_year = min(birth for birth, death in logs)
        max_year = max(death for birth, death in logs)

        # Initialize an array to track population changes
        population_changes = [0] * (max_year - min_year + 1)

        # Process each log to update population changes
        for birth, death in logs:
            population_changes[birth - min_year] += 1
            population_changes[death - min_year] -= 1

        # Calculate the maximum population year by accumulating changes
        max_population = 0
        max_year_with_max_population = min_year
        current_population = 0

        for year in range(max_year - min_year + 1):
            current_population += population_changes[year]
            if current_population > max_population:
                max_population = current_population
                max_year_with_max_population = min_year + year

        return max_year_with_max_population


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [[1993, 1999], [2000, 2010]],  # Expected: 1993
        [[1950, 1961], [1960, 1971], [1970, 1981]],  # Expected: 1960
        [[1993, 1999], [2000, 2010], [1975, 2005], [1975, 2003], [1803, 1809], [
            1750, 1869], [1840, 1935], [1803, 1921], [1894, 1921]]  # Expected: 1894
    ]

    for i, logs in enumerate(test_cases):
        result = solution.maximumPopulation(logs)
        print(f"Test case {i + 1}:")
        print("Birth/Death logs:")
        for birth, death in logs:
            print(f"  Person born in {birth}, died in {death}")
        print(f"Year with maximum population: {result}")

        # Show population by year for verification
        min_year = min(birth for birth, death in logs)
        max_year = max(death for birth, death in logs)
        population = {}
        for year in range(min_year, max_year):
            count = sum(1 for birth, death in logs if birth <= year < death)
            if count > 0:
                population[year] = count
        print("Population by year:")
        for year, count in sorted(population.items()):
            print(f"  Year {year}: {count} people")
        print()
