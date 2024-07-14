from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque

    # Create a graph as an adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # States: 0 = unknown, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def hasCycle(v):
            if state[v] == 1:
                return True
            if state[v] == 2:
                return False

            # Mark the node as visiting
            state[v] = 1
            for neighbor in graph[v]:
                if hasCycle(neighbor):
                    return True

            # Mark the node as visited
            state[v] = 2
            return False

        # Check for cycles in each component of the graph
        for v in range(numCourses):
            if hasCycle(v):
                return False

        return True
