package amazon;

import java.util.*;

public class FrogPosition1377 {
    public double frogPosition(int n, int[][] edges, int t, int target) {
        // Build adjacency list for the graph representation of the tree
        List<Integer>[] graph = new List[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        // DFS function to calculate probability
        return dfs(graph, 1, -1, t, 1.0, target);
    }

    private double dfs(List<Integer>[] graph, int node, int parent, int time, double prob, int target) {
        if (node == target) {
            if (time == 0 || graph[node].size() == 1 && node != 1) {
                return prob;
            }
            return 0;
        }

        if (time == 0) {
            return 0;
        }

        List<Integer> children = new ArrayList<>();
        for (int child : graph[node]) {
            if (child != parent) {
                children.add(child);
            }
        }

        if (children.isEmpty()) {
            return 0;
        }

        double probPerChild = prob / children.size();
        for (int child : children) {
            double result = dfs(graph, child, node, time - 1, probPerChild, target);
            if (result > 0) {
                return result;
            }
        }

        return 0;
    }

    // Testing
    public static void main(String[] args) {
        FrogPosition1377 solution = new FrogPosition1377();
        int n = 7;
        int[][] edges = {{1, 2}, {1, 3}, {1, 7}, {2, 4}, {2, 6}, {3, 5}};
        int t = 2;
        int target = 4;
        System.out.println("Java Test Result: " + solution.frogPosition(n, edges, t, target));  // Output should be 0.3333 (1/3)
    }
}

