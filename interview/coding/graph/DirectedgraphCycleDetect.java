package graph;

import java.util.*;

public class DirectedgraphCycleDetect {
    private final int V; // Number of vertices
    private final List<List<Integer>> adj; // Adjacency list

    // Constructor
    public DirectedgraphCycleDetect(int V) {
        this.V = V;
        adj = new ArrayList<>(V);
        for (int i = 0; i < V; i++) {
            adj.add(new LinkedList<>());
        }
    }

    // Function to add an edge into the graph
    void addEdge(int source, int dest) {
        adj.get(source).add(dest);
    }

    // Function to detect cycle in the graph
    boolean isCyclic() {
        // Mark all the vertices as not visited
        boolean[] visited = new boolean[V];
        // Stack to keep track of the vertices in the current recursion stack
        boolean[] recStack = new boolean[V];

        // Call the recursive helper function to detect cycle in different DFS trees
        for (int i = 0; i < V; i++) {
            if (!visited[i] && isCyclicUtil(i, visited, recStack)) {
                return true;
            }
        }

        return false;
    }

    // Recursive function to detect cycle in a graph
    private boolean isCyclicUtil(int v, boolean[] visited, boolean[] recStack) {
        // Mark the current node as visited and part of the recursion stack
        visited[v] = true;
        recStack[v] = true;

        // Recur for all the vertices adjacent to this vertex
        for (Integer neighbor : adj.get(v)) {
            if (!visited[neighbor] && isCyclicUtil(neighbor, visited, recStack)) {
                return true;
            } else if (recStack[neighbor]) {
                return true;
            }
        }

        // Remove the vertex from recursion stack
        recStack[v] = false;

        return false;
    }

    public static void main(String[] args) {
        DirectedgraphCycleDetect graph = new DirectedgraphCycleDetect(4);

        graph.addEdge(0, 1);
        graph.addEdge(0, 2);
        graph.addEdge(1, 2);
        graph.addEdge(2, 0);
        graph.addEdge(2, 3);
        graph.addEdge(3, 3);

        if (graph.isCyclic()) {
            System.out.println("Graph contains cycle");
        } else {
            System.out.println("Graph doesn't contain cycle");
        }
    }
}
