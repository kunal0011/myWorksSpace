package amazon;

import java.util.*;

public class Rabbitsinforest781 {
    public int numRabbits(int[] answers) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int answer : answers) {
            count.put(answer, count.getOrDefault(answer, 0) + 1);
        }

        int totalRabbits = 0;

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            int answer = entry.getKey();
            int numRabbits = entry.getValue();
            int groupSize = answer + 1;  // Group size is answer + 1
            int groupsNeeded = (numRabbits + groupSize - 1) / groupSize;  // How many full groups needed
            totalRabbits += groupsNeeded * groupSize;  // Add the rabbits from all groups
        }

        return totalRabbits;
    }

    // Test cases
    public static void main(String[] args) {
        Rabbitsinforest781 sol = new Rabbitsinforest781();

        // Test case 1
        int[] answers1 = {1, 1, 2};
        System.out.println(sol.numRabbits(answers1));  // Expected output: 5

        // Test case 2
        int[] answers2 = {10, 10, 10};
        System.out.println(sol.numRabbits(answers2));  // Expected output: 11

        // Test case 3
        int[] answers3 = {};
        System.out.println(sol.numRabbits(answers3));  // Expected output: 0
    }
}

