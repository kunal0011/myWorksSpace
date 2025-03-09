"""
LeetCode 207 - Course Schedule

Problem Statement:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example, to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1].
Given numCourses and prerequisites array, return true if you can finish all courses.

Solution Logic:
1. Use Kahn's Algorithm (Topological Sort):
   - Build adjacency list and track in-degree for each course
   - Start with courses having no prerequisites (in-degree = 0)
   - Process each available course and reduce in-degree of dependent courses
   - If we can process all courses, no cycle exists (return True)
   - If we can't process all courses, cycle exists (return False)

Time Complexity: O(V + E) where V = number of courses, E = number of prerequisites
Space Complexity: O(V + E) for storing the graph and queue
"""

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

def run_test_cases():
    """Test driver with various test scenarios"""
    solution = Solution()
    
    test_cases = [
        {
            "input": {"numCourses": 2, "prerequisites": [[1,0]]},
            "expected": True,
            "description": "Simple linear dependency"
        },
        {
            "input": {"numCourses": 2, "prerequisites": [[1,0],[0,1]]},
            "expected": False,
            "description": "Cycle between two courses"
        },
        {
            "input": {"numCourses": 4, "prerequisites": [[1,0],[2,1],[3,2]]},
            "expected": True,
            "description": "Linear chain dependency"
        },
        {
            "input": {"numCourses": 3, "prerequisites": []},
            "expected": True,
            "description": "No prerequisites"
        },
        {
            "input": {"numCourses": 4, "prerequisites": [[1,0],[2,1],[3,2],[1,3]]},
            "expected": False,
            "description": "Complex cycle"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        input_data = test["input"]
        result = solution.canFinish(**input_data)
        assert result == test["expected"], f"""
        Test {i} Failed: {test['description']}
        Expected: {test['expected']}
        Got: {result}
        Input: {input_data}
        """
        print(f"Test {i} Passed: {test['description']}")

if __name__ == "__main__":
    run_test_cases()
