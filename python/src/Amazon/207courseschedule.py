from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Create a graph and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # Build the graph and fill in-degrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize the queue with nodes having zero in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # Count of courses that have been processed
        count = 0

        # Process nodes with zero in-degree
        while queue:
            course = queue.popleft()
            count += 1

            # Decrease in-degree for all neighbors
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes zero, add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If we processed all courses, return True
        return count == numCourses
