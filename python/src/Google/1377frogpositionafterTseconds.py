"""
LeetCode 1377: Frog Position After T Seconds

Problem Statement:
Given an undirected tree with n vertices numbered from 1 to n, and a target vertex.
A frog starts at vertex 1 and wants to reach the target vertex in exactly t seconds.
During each second, the frog:
1. If at vertex u, jumps to one of its unvisited neighbors v with equal probability
2. Once the frog reaches target or t seconds pass, it stops moving
Return probability that frog is on target vertex after exactly t seconds

Logic:
1. Build undirected tree using adjacency list
2. Use DFS with parameters:
   - node: current node
   - parent: parent node to avoid backtracking
   - time: remaining time
   - prob: current probability
3. Base cases:
   - If time=0 or leaf node reached: return prob if at target, else 0
4. For each unvisited neighbor:
   - Calculate probability by dividing current prob by number of valid moves
   - Recursively explore with updated probability and decremented time
5. Return 0 if target not reachable

Time Complexity: O(N) where N is number of nodes
Space Complexity: O(N) for adjacency list and recursion stack
"""

from collections import defaultdict


class Solution:
    def frogPosition(self, n: int, edges: list[list[int]], t: int, target: int) -> float:
        # Build the tree as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS to find the probability of reaching the target at time t
        def dfs(node: int, parent: int, time: int, prob: float) -> float:
            # If no more moves possible
            if time == 0 or len(graph[node]) == (1 if node != 1 else 0):
                return prob if node == target else 0.0

            # Number of valid next moves
            count = len(graph[node]) - (1 if node != 1 else 0)
            for neighbor in graph[node]:
                if neighbor != parent:  # Avoid going back to the parent node
                    result = dfs(neighbor, node, time - 1, prob / count)
                    if result > 0:  # If the result is non-zero, we've reached the target
                        return result

            return 0.0

        # Start DFS from the root node (1) with probability 1.0
        return dfs(1, -1, t, 1.0)


def test_frog_position():
    solution = Solution()

    # Test case 1: Basic tree
    n1, edges1, t1, target1 = 7, [[1, 2], [1, 3],
                                  [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4
    result1 = solution.frogPosition(n1, edges1, t1, target1)
    expected1 = 0.16666666666666666
    assert abs(
        result1 - expected1) < 1e-5, f"Test case 1 failed. Expected {expected1}, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: Target is root
    n2, edges2, t2, target2 = 1, [], 1, 1
    result2 = solution.frogPosition(n2, edges2, t2, target2)
    expected2 = 1.0
    assert abs(
        result2 - expected2) < 1e-5, f"Test case 2 failed. Expected {expected2}, got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Not enough time
    n3, edges3, t3, target3 = 3, [[2, 1], [3, 2]], 1, 3
    result3 = solution.frogPosition(n3, edges3, t3, target3)
    expected3 = 0.0
    assert abs(
        result3 - expected3) < 1e-5, f"Test case 3 failed. Expected {expected3}, got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Extra time at leaf
    n4, edges4, t4, target4 = 4, [[1, 2], [2, 3], [3, 4]], 4, 4
    result4 = solution.frogPosition(n4, edges4, t4, target4)
    expected4 = 1.0
    assert abs(
        result4 - expected4) < 1e-5, f"Test case 4 failed. Expected {expected4}, got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_frog_position()
