"""
LeetCode 399: Evaluate Division

Problem Statement:
You are given an array of variable pairs equations and an array of real numbers values, where 
equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where 
you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Example:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
       queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.0, 0.5, -1.0, 1.0, -1.0]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0]

Time Complexity: O(N + Q*V) where N is number of equations, Q is number of queries, V is number of variables
Space Complexity: O(V) where V is number of variables in equations
"""

from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build graph representation
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        def dfs(start: str, end: str, visited: set) -> float:
            # Base cases
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            # Mark current node as visited
            visited.add(start)
            
            # Explore all neighbors
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result
            
            return -1.0
        
        # Process each query using DFS
        return [dfs(start, end, set()) for start, end in queries]

def test_evaluate_division():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()
    
    test_cases = [
        {
            "equations": [["a","b"],["b","c"]],
            "values": [2.0, 3.0],
            "queries": [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],
            "expected": [6.0, 0.5, -1.0, 1.0, -1.0],
            "description": "Basic case with chain of equations"
        },
        {
            "equations": [["a","b"],["b","c"],["bc","cd"]],
            "values": [1.5, 2.5, 5.0],
            "queries": [["a","c"],["c","b"],["bc","cd"],["cd","bc"]],
            "expected": [3.75, 0.4, 5.0, 0.2],
            "description": "Multiple connected components"
        },
        {
            "equations": [["a","b"]],
            "values": [0.5],
            "queries": [["a","b"],["b","a"],["a","c"],["x","y"]],
            "expected": [0.5, 2.0, -1.0, -1.0],
            "description": "Single equation with invalid queries"
        },
        {
            "equations": [["x","x"]],
            "values": [1.0],
            "queries": [["x","x"]],
            "expected": [1.0],
            "description": "Self division"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        equations = test_case["equations"]
        values = test_case["values"]
        queries = test_case["queries"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Equations: {equations}")
        print(f"Values: {values}")
        print(f"Queries: {queries}")
        
        result = solution.calcEquation(equations, values, queries)
        
        # Compare results with tolerance for floating point
        for r, e in zip(result, expected):
            if r == -1.0 and e == -1.0:
                continue
            assert abs(r - e) < 1e-5, f"Expected {e}, but got {r}"
        
        print(f"✓ Test case passed! Output: {result}")

if __name__ == "__main__":
    test_evaluate_division()
    print("\nAll test cases passed! 🎉")
