from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a graph as an adjacency list
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build the graph and calculate in-degrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Queue for courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If the order contains all courses, return it. Otherwise, return an empty array.
        return order if len(order) == numCourses else []


# Example usage
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# Output: [0,1,2,3] or any valid topological order
s = Solution()
print(s.findOrder(numCourses, prerequisites))
