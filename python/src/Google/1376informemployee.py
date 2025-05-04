"""
LeetCode 1376: Time Needed to Inform All Employees

Problem Statement:
A company has n employees with unique IDs from 0 to n-1. The head of the company has ID headID.
Each employee has one direct manager given in manager array where manager[i] is the direct manager
of the i-th employee. The head of the company has no manager (manager[headID] = -1).
Each employee needs informTime[i] minutes to inform all their subordinates about the news.
Return the number of minutes needed to inform all employees about the news.

Logic:
1. Build an adjacency list representation of the company hierarchy
   - Key: manager ID
   - Value: list of direct subordinates
2. Use DFS to traverse the tree and calculate time:
   - Base case: employee has no subordinates (return 0)
   - For each employee:
     * Find max time needed among all subordinates
     * Add current employee's inform time
3. Result is the maximum path from root to any leaf

Time Complexity: O(n) where n is number of employees
Space Complexity: O(n) for adjacency list and recursion stack
"""

from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create adjacency list for the tree
        subordinates = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)

        def dfs(employee: int) -> int:
            # Base case: leaf node (no subordinates)
            if employee not in subordinates:
                return 0

            # Find max time needed among all subordinates
            max_subordinate_time = 0
            for subordinate in subordinates[employee]:
                max_subordinate_time = max(
                    max_subordinate_time, dfs(subordinate))

            # Return total time: time to inform current employee's subordinates + max time for subordinates
            return informTime[employee] + max_subordinate_time

        return dfs(headID)


def test_inform_employees():
    solution = Solution()

    # Test case 1: Simple hierarchy
    n1, headID1 = 6, 2
    manager1 = [2, 2, -1, 2, 2, 2]
    informTime1 = [0, 0, 1, 0, 0, 0]
    result1 = solution.numOfMinutes(n1, headID1, manager1, informTime1)
    assert result1 == 1, f"Test case 1 failed. Expected 1, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: Multiple levels
    n2, headID2 = 7, 6
    manager2 = [1, 2, 3, 4, 5, 6, -1]
    informTime2 = [0, 6, 5, 4, 3, 2, 1]
    result2 = solution.numOfMinutes(n2, headID2, manager2, informTime2)
    assert result2 == 21, f"Test case 2 failed. Expected 21, got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Single employee
    n3, headID3 = 1, 0
    manager3 = [-1]
    informTime3 = [0]
    result3 = solution.numOfMinutes(n3, headID3, manager3, informTime3)
    assert result3 == 0, f"Test case 3 failed. Expected 0, got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Star topology
    n4, headID4 = 4, 2
    manager4 = [2, 2, -1, 2]
    informTime4 = [0, 0, 4, 0]
    result4 = solution.numOfMinutes(n4, headID4, manager4, informTime4)
    assert result4 == 4, f"Test case 4 failed. Expected 4, got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_inform_employees()
