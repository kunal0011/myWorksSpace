package amazon;

 import java.util.*;

public class MinimumSemester1136 {
    public int minimumSemesters(int n, int[][] relations) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] indegree = new int[n + 1];

        // Initialize graph
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        // Build the graph and indegree array
        for (int[] relation : relations) {
            int pre = relation[0], course = relation[1];
            graph.get(pre).add(course);
            indegree[course]++;
        }

        // Queue for BFS
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        int semesters = 0;
        int completedCourses = 0;

        // Perform topological sort with BFS
        while (!queue.isEmpty()) {
            semesters++;
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                int course = queue.poll();
                completedCourses++;

                for (int neighbor : graph.get(course)) {
                    indegree[neighbor]--;
                    if (indegree[neighbor] == 0) {
                        queue.offer(neighbor);
                    }
                }
            }
        }

        return completedCourses == n ? semesters : -1;
    }
}
