from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
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


# Example usage
solution = Solution()
logs = [[1993, 1999], [2000, 2010], [1975, 2005], [1975, 2003], [
    1803, 1809], [1750, 1869], [1840, 1935], [1803, 1921], [1894, 1921]]
print(solution.maximumPopulation(logs))  # Output: 1960
