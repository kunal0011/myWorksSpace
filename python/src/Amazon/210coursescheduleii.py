"""
LeetCode 210 - Course Schedule II

Problem Statement:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.
Return the ordering of courses you should take to finish all courses. If there are many valid 
answers, return any of them. If it is impossible to finish all courses, return an empty array.

Solution Logic:
1. Use Topological Sort with Kahn's Algorithm
2. Build adjacency list and calculate in-degree for each node
3. Start with nodes having 0 in-degree (no prerequisites)
4. Process each course, reducing in-degree of dependent courses
5. If cycle exists, some courses will remain with in-degree > 0
6. Time: O(V + E), Space: O(V + E) where V is courses and E is prerequisites
"""

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

def test_course_schedule():
    solution = Solution()
    
    # Test Case 1: Simple valid case
    num_courses1 = 4
    prerequisites1 = [[1,0],[2,0],[3,1],[3,2]]
    result1 = solution.findOrder(num_courses1, prerequisites1)
    print("Test 1: Valid course schedule")
    print(f"Number of courses: {num_courses1}")
    print(f"Prerequisites: {prerequisites1}")
    print(f"Course order: {result1}")  # Expected: [0,1,2,3] or [0,2,1,3]
    
    # Test Case 2: No prerequisites
    num_courses2 = 3
    prerequisites2 = []
    result2 = solution.findOrder(num_courses2, prerequisites2)
    print("\nTest 2: No prerequisites")
    print(f"Number of courses: {num_courses2}")
    print(f"Prerequisites: {prerequisites2}")
    print(f"Course order: {result2}")  # Expected: [0,1,2] (any order)
    
    # Test Case 3: Impossible case (cycle)
    num_courses3 = 2
    prerequisites3 = [[1,0],[0,1]]
    result3 = solution.findOrder(num_courses3, prerequisites3)
    print("\nTest 3: Impossible schedule (cycle)")
    print(f"Number of courses: {num_courses3}")
    print(f"Prerequisites: {prerequisites3}")
    print(f"Course order: {result3}")  # Expected: []

if __name__ == "__main__":
    test_course_schedule()
