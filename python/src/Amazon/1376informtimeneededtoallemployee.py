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
