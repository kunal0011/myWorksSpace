from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Build the adjacency list for the company hierarchy
        graph = defaultdict(list)
        for employee in range(n):
            # Skip if the manager is -1 (which means no manager)
            if manager[employee] != -1:
                graph[manager[employee]].append(employee)

        # Helper function to perform DFS
        def dfs(employee: int) -> int:
            # Base case: if the employee has no direct reports
            if not graph[employee]:
                return 0
            # Calculate the maximum time required to inform all direct reports
            max_time = 0
            for report in graph[employee]:
                max_time = max(max_time, dfs(report))
            return informTime[employee] + max_time

        # Start DFS from the headID
        return dfs(headID)
    
def test_inform_time():
    solution = Solution()
    
    # Test Case 1: Simple tree
    # assert solution.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]) == 1
    
    # Test Case 2: Linear chain
    assert solution.numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]) == 21
    
    # Test Case 3: Single employee
    # assert solution.numOfMinutes(1, 0, [-1], [0]) == 0
    
    # # Test Case 4: Star topology
    # assert solution.numOfMinutes(4, 0, [-1,0,0,0], [1,0,0,0]) == 1
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_inform_time()
