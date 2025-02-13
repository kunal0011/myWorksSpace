"""
LeetCode 133. Clone Graph

Problem Statement:
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and so on.
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: 
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list [].
The graph consists of only one node with val = 1 and it does not have any neighbors.

Constraints:
- The number of nodes in the graph is in the range [0, 100]
- 1 <= Node.val <= 100
- Node.val is unique for each node
- There are no repeated edges and no self-loops in the graph
- The Graph is connected and all nodes can be visited starting from the given node
"""

from typing import Optional, List, Dict, Set
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        DFS approach with hash map.
        Time complexity: O(N + E) where N is number of nodes and E is number of edges
        Space complexity: O(N) for the hash map
        """
        if not node:
            return None

        # Hash map to store cloned nodes: original node -> cloned node
        cloned = {}

        def dfs(node: 'Node') -> 'Node':
            # If node already cloned, return its clone
            if node in cloned:
                return cloned[node]

            # Create new node and add to hash map
            clone = Node(node.val)
            cloned[node] = clone

            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

    def cloneGraphBFS(self, node: Optional['Node']) -> Optional['Node']:
        """
        BFS approach.
        Time complexity: O(N + E)
        Space complexity: O(N)
        """
        if not node:
            return None

        # Create clone of first node
        clone = Node(node.val)
        cloned = {node: clone}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            # Process all neighbors
            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    # Create new node if not seen before
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Add neighbor to current node's clone
                cloned[curr].neighbors.append(cloned[neighbor])

        return clone


def create_graph(adjList: List[List[int]]) -> Optional[Node]:
    """Helper function to create graph from adjacency list."""
    if not adjList:
        return None

    # Create all nodes
    nodes = {i+1: Node(i+1) for i in range(len(adjList))}

    # Add neighbors
    for i, neighbors in enumerate(adjList, 1):
        nodes[i].neighbors = [nodes[n] for n in neighbors]

    return nodes[1] if nodes else None


def get_adjacency_list(node: Optional[Node]) -> List[List[int]]:
    """Helper function to convert graph to adjacency list."""
    if not node:
        return []

    adj_list = []
    visited = set()
    node_to_index = {}

    def dfs(node: 'Node') -> None:
        if node in visited:
            return

        visited.add(node)
        index = len(adj_list)
        node_to_index[node] = index
        adj_list.append([])

        for neighbor in node.neighbors:
            if neighbor not in node_to_index:
                dfs(neighbor)
            adj_list[index].append(neighbor.val)

    dfs(node)
    return adj_list


def visualize_graph(node: Optional[Node]) -> None:
    """Helper function to visualize graph structure."""
    if not node:
        print("Empty graph")
        return

    visited = set()

    def dfs(node: 'Node', depth: int = 0) -> None:
        if node in visited:
            return

        visited.add(node)
        indent = "  " * depth
        neighbors = [n.val for n in node.neighbors]
        print(f"{indent}Node {node.val} -> neighbors: {neighbors}")

        for neighbor in node.neighbors:
            if neighbor not in visited:
                dfs(neighbor, depth + 1)

    print("\nGraph structure:")
    dfs(node)


def test_clone_graph():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "adjList": [[2, 4], [1, 3], [2, 4], [1, 3]],
            "description": "Standard connected graph"
        },
        {
            "adjList": [[]],
            "description": "Single node without neighbors"
        },
        {
            "adjList": [[2], [1]],
            "description": "Two connected nodes"
        },
        {
            "adjList": [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]],
            "description": "Fully connected graph"
        },
        {
            "adjList": [],
            "description": "Empty graph"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input adjacency list: {test_case['adjList']}")

        # Create original graph
        original = create_graph(test_case['adjList'])
        print("\nOriginal graph:")
        visualize_graph(original)

        # Test both implementations
        cloned1 = solution.cloneGraph(original)
        cloned2 = solution.cloneGraphBFS(original)

        # Convert back to adjacency lists
        result1 = get_adjacency_list(cloned1)
        result2 = get_adjacency_list(cloned2)

        print("\nCloned graph (DFS):")
        visualize_graph(cloned1)
        print("\nCloned graph (BFS):")
        visualize_graph(cloned2)

        # Verify results
        assert result1 == test_case['adjList'], \
            f"DFS cloning failed. Expected {test_case['adjList']}, got {result1}"
        assert result2 == test_case['adjList'], \
            f"BFS cloning failed. Expected {test_case['adjList']}, got {result2}"

        # Verify deep copy
        if original:
            assert cloned1 is not original, "DFS clone is not a deep copy"
            assert cloned2 is not original, "BFS clone is not a deep copy"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_clone_graph()
