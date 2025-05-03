"""
LeetCode 399 - Evaluate Division

Problem Statement:
You are given an array of variable pairs equations and an array of real numbers values, where 
equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
Each Ai or Bi is a string that represents a single variable.

You are also given an array of queries, where queries[j] = [Cj, Dj] represents the jth query 
where you must find the answer for Cj / Dj.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Time Complexity: O(N + Q*N) where N is number of equations and Q is number of queries
Space Complexity: O(N) for the graph
"""
from collections import defaultdict
from typing import List

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    # Build graph
    graph = defaultdict(dict)
    for (x, y), val in zip(equations, values):
        graph[x][y] = val
        graph[y][x] = 1.0 / val
    
    def dfs(start: str, end: str, visited: set) -> float:
        # If either node doesn't exist in graph
        if start not in graph or end not in graph:
            return -1.0
            
        # Direct connection exists
        if end in graph[start]:
            return graph[start][end]
            
        # Mark current node as visited
        visited.add(start)
        
        # Try all possible paths
        for neighbor in graph[start]:
            if neighbor not in visited:
                # Try to find path through this neighbor
                temp = dfs(neighbor, end, visited)
                if temp != -1.0:
                    return graph[start][neighbor] * temp
                    
        return -1.0
    
    # Process each query
    result = []
    for start, end in queries:
        result.append(dfs(start, end, set()))
    
    return result

def test_evaluate_division():
    # Test Case 1
    equations1 = [["a","b"],["b","c"]]
    values1 = [2.0,3.0]
    queries1 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    expected1 = [6.0, 0.5, -1.0, 1.0, -1.0]
    result1 = calcEquation(equations1, values1, queries1)
    print(f"Test Case 1:")
    print(f"Input: equations = {equations1}, values = {values1}, queries = {queries1}")
    print(f"Expected: {expected1}")
    print(f"Output: {result1}")
    print(f"Pass: {result1 == expected1}\n")

    # Test Case 2
    equations2 = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values2 = [3.0,4.0,5.0,6.0]
    queries2 = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    expected2 = [360.0, 0.008333333333333333, 20.0, 1.0, -1.0, -1.0]
    result2 = calcEquation(equations2, values2, queries2)
    print(f"Test Case 2:")
    print(f"Input: equations = {equations2}, values = {values2}, queries = {queries2}")
    print(f"Expected: {expected2}")
    print(f"Output: {result2}")
    print(f"Pass: {result2 == expected2}")

if __name__ == "__main__":
    test_evaluate_division()