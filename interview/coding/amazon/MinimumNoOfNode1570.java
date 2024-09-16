package amazon;

import java.util.ArrayList;
import java.util.List;

public class MinimumNoOfNode1570 {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        // Step 1: Initialize an array to keep track of in-degrees
        int[] inDegree = new int[n];

        // Step 2: Calculate the in-degree of each node
        for (List<Integer> edge : edges) {
            int v = edge.get(1);
            inDegree[v]++;
        }

        // Step 3: Collect all nodes with zero in-degree
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                result.add(i);
            }
        }

        return result;
    }

    // Testing
    public static void main(String[] args) {
        MinimumNoOfNode1570 solution = new MinimumNoOfNode1570();
        List<List<Integer>> edges = new ArrayList<>();
//        edges.add(List.of(0, 1));
//        edges.add(List.of(0, 2));
//        edges.add(List.of(2, 5));
//        edges.add(List.of(3, 4));
//        edges.add(List.of(4, 2));

        System.out.println("Java Test Result: " + solution.findSmallestSetOfVertices(6, edges));  // Output should be [0, 3]
    }
}
