package amazon;

import java.util.HashMap;

public class MinimumRoundToCompleteTask {
    public int minimumRounds(int[] tasks) {
        HashMap<Integer, Integer> taskCount = new HashMap<>();
        int rounds = 0;

        // Count frequency of each task difficulty
        for (int task : tasks) {
            taskCount.put(task, taskCount.getOrDefault(task, 0) + 1);
        }

        // Calculate the minimum rounds required
        for (int count : taskCount.values()) {
            if (count == 1) {
                return -1;  // Impossible to complete this difficulty
            }

            // Maximize the use of rounds with 3 tasks
            rounds += count / 3;
            if (count % 3 != 0) {
                rounds += 1;  // Add one more round to complete the remaining tasks
            }
        }

        return rounds;
    }

    public static void main(String[] args) {
        MinimumRoundToCompleteTask task = new MinimumRoundToCompleteTask();
        System.out.println(task.minimumRounds(new int[]{2,2,3,3,3,3,4,4,5,5}));
    }
}
