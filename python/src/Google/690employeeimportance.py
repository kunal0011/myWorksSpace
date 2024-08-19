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
