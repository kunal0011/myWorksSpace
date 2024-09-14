package amazon;

import java.util.*;

public class QueryOnPermutaion1409{
    public List<Integer> processQueries(int[] queries, int m) {
        // Initialize the permutation list
        List<Integer> perm = new ArrayList<>();
        for (int i = 1; i <= m; i++) {
            perm.add(i);
        }

        List<Integer> result = new ArrayList<>();

        // Process each query
        for (int q : queries) {
            int index = perm.indexOf(q);  // Find the index of the query element
            result.add(index);           // Add the index to the result
            perm.remove(index);          // Remove the element from its current position
            perm.add(0, q);              // Insert the element at the front of the list
        }

        return result;
    }
}
