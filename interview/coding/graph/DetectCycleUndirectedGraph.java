package graph;

import java.util.*;

public class DetectCycleUndirectedGraph {
    private final int V; // Number of vertices
    private final List<List<Integer>> adj; // Adjacency list

    // Constructor
    public DetectCycleUndirectedGraph(int V) {
        this.V = V;
        adj = new ArrayList<>(V);
        for (int i = 0; i < V; i++) {
            adj.add(new LinkedList<>());
        }
    }

    // Function to add an edge into the graph
    void addEdge(int source, int dest) {
        adj.get(source).add(dest);
        adj.get(dest).add(source); // Since the graph is undirected
    }

    // Function to detect cycle in the graph
    boolean isCyclic() {
        // Mark all the vertices as not visited
        boolean[] visited = new boolean[V];

        // Call the recursive helper function to detect cycle in different DFS trees
        for (int i = 0; i < V; i++) {
            if (!visited[i] && isCyclicUtil(i, visited, -1)) {
                return true;
            }
        }

        return false;
    }

    // Recursive function to detect cycle in a graph
    private boolean isCyclicUtil(int v, boolean[] visited, int parent) {
        // Mark the current node as visited
        visited[v] = true;

        // Recur for all the vertices adjacent to this vertex
        for (Integer neighbor : adj.get(v)) {
            // If an adjacent vertex is not visited, then recur for that adjacent
            if (!visited[neighbor]) {
                if (isCyclicUtil(neighbor, visited, v)) {
                    return true;
                }
            }
            // If an adjacent vertex is visited and not parent of the current vertex, then there is a cycle
            else if (neighbor != parent) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        DetectCycleUndirectedGraph graph = new DetectCycleUndirectedGraph(5);

        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(3, 4);

        if (graph.isCyclic()) {
            System.out.println("Graph contains cycle");
        } else {
            System.out.println("Graph doesn't contain cycle");
        }
    }
}
