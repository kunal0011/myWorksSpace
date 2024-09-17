from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # Build graph and indegree array
        graph = defaultdict(list)
        indegree = [0] * (n + 1)

        for pre, course in relations:
            graph[pre].append(course)
            indegree[course] += 1

        # Queue for BFS
        queue = deque()
        for i in range(1, n + 1):
            if indegree[i] == 0:
                queue.append(i)

        semesters = 0
        completed_courses = 0

        # Perform topological sort with BFS
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                course = queue.popleft()
                completed_courses += 1

                for neighbor in graph[course]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        return semesters if completed_courses == n else -1
