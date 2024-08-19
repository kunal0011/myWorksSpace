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

# Example usage
# Let's create a graph with 4 nodes connected in a square:

# Node 1 neighbors: Node 2, Node 4
# Node 2 neighbors: Node 1, Node 3
# Node 3 neighbors: Node 2, Node 4
# Node 4 neighbors: Node 1, Node 3


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
cloned_graph = solution.cloneGraph(node1)

# To verify the deep copy, you can check that the cloned nodes are not the same as the original nodes:
print(cloned_graph.val)  # Should print 1 (root node's value)
# Should print 2 (first neighbor of the root node)
print(cloned_graph.neighbors[0].val)
# Should print 4 (second neighbor of the root node)
print(cloned_graph.neighbors[1].val)
