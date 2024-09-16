from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        # Step 1: Find min and max salaries
        min_salary = min(salary)
        max_salary = max(salary)

        # Step 2: Calculate total sum of salaries
        total_sum = sum(salary)

        # Step 3: Exclude min and max salaries
        total_sum -= (min_salary + max_salary)

        # Step 4: Calculate the average of remaining salaries
        count = len(salary) - 2
        return total_sum / count


# Testing
solution = Solution()
salary = [4000, 3000, 1000, 2000]
print("Python Test Result:", solution.average(
    salary))  # Output should be 2500.0
