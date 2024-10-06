class Node:
    def __init__(self, val: int = 0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # If the node was already visited before, return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # Create a new node with the value of the old node (without neighbors for now)
        clone_node = Node(node.val, [])

        # Save the clone node to the visited dictionary
        self.visited[node] = clone_node

        # Iterate through the neighbors to clone them
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
