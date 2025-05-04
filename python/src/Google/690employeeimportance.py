"""
LeetCode 690: Employee Importance
Problem Statement:
You have a data structure of employee information, including the employee's unique ID, 
their importance value, and their direct subordinates' IDs.
Given an employee ID, return the total importance value of this employee and all their subordinates.

Logic:
1. Create a hashmap for O(1) lookup of employees by their ID
2. Use DFS (Depth-First Search) to traverse the employee hierarchy
3. For each employee:
   - Add their importance value
   - Recursively add importance of all subordinates
4. Return total accumulated importance

Time Complexity: O(N) where N is the number of employees
Space Complexity: O(N) for hashmap and recursion stack
"""

from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        # Step 1: Create a dictionary to map employee ID to the Employee object
        employee_map = {e.id: e for e in employees}

        # Step 2: Define the DFS function
        def dfs(eid: int) -> int:
            # Get the employee object using the ID
            employee = employee_map[eid]

            # Start with the employee's own importance
            total_importance = employee.importance

            # Step 3: Add the importance of all subordinates recursively
            for sub_id in employee.subordinates:
                total_importance += dfs(sub_id)

            # Return the accumulated total importance
            return total_importance

        # Step 4: Start DFS from the given employee ID
        return dfs(id)


def test_employee_importance():
    # Create test employees
    emp1 = Employee(1, 5, [2, 3])  # Boss with importance 5
    emp2 = Employee(2, 3, [])      # Subordinate 1 with importance 3
    emp3 = Employee(3, 3, [])      # Subordinate 2 with importance 3

    # Test Case 1: Normal hierarchy
    solution = Solution()
    result1 = solution.getImportance([emp1, emp2, emp3], 1)
    assert result1 == 11, f"Expected 11, but got {result1}"
    print("Test case 1: Basic hierarchy with boss and two subordinates ✓")

    # Test Case 2: Single employee
    result2 = solution.getImportance([emp2], 2)
    assert result2 == 3, f"Expected 3, but got {result2}"
    print("Test case 2: Single employee with no subordinates ✓")

    # Test Case 3: Complex hierarchy
    emp4 = Employee(4, 10, [5, 6])
    emp5 = Employee(5, 5, [])
    emp6 = Employee(6, 5, [7])
    emp7 = Employee(7, 3, [])
    result3 = solution.getImportance([emp4, emp5, emp6, emp7], 4)
    assert result3 == 23, f"Expected 23, but got {result3}"
    print("Test case 3: Complex hierarchy with multiple levels ✓")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_employee_importance()
