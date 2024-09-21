package amazon;

import java.util.*;

public class RedundantConnectionii685 {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int[] parent = new int[edges.length + 1];
        int[] candidate1 = null;
        int[] candidate2 = null;

        // Step 1: Check whether there is a node with two parents
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            if (parent[v] != 0) {
                candidate1 = new int[]{parent[v], v};
                candidate2 = new int[]{u, v};
                edge[1] = 0;  // Invalidate the second edge temporarily
            } else {
                parent[v] = u;
            }
        }

        // Union-Find to detect cycles
        int[] uf = new int[edges.length + 1];
        for (int i = 0; i < uf.length; i++) {
            uf[i] = i;
        }

        for (int[] edge : edges) {
            if (edge[1] == 0) continue;  // Skip the invalidated edge
            int u = edge[0], v = edge[1];
            if (find(uf, u) == v) {
                if (candidate1 != null) {
                    return candidate1;  // There is a cycle and a node with two parents
                }
                return edge;  // Return the edge that caused the cycle
            }
            union(uf, u, v);
        }

        return candidate2;
    }

    private int find(int[] uf, int x) {
        if (uf[x] != x) {
            uf[x] = find(uf, uf[x]);
        }
        return uf[x];
    }

    private void union(int[] uf, int x, int y) {
        uf[find(uf, y)] = find(uf, x);
    }

    // Test cases
    public static void main(String[] args) {
        RedundantConnectionii685 sol = new RedundantConnectionii685();

        // Test case 1
        int[][] edges1 = {{1, 2}, {1, 3}, {2, 3}};
        System.out.println(Arrays.toString(sol.findRedundantDirectedConnection(edges1)));  // Output: [2, 3]

        // Test case 2
        int[][] edges2 = {{1, 2}, {2, 3}, {3, 4}, {4, 1}, {1, 5}};
        System.out.println(Arrays.toString(sol.findRedundantDirectedConnection(edges2)));  // Output: [4, 1]
    }
}
