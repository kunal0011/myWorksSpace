package amazon;

public class Dietperformance1176 {
    public int dietPlanPerformance(int[] calories, int k, int lower, int upper) {
        int score = 0;
        int currentSum = 0;

        // Calculate sum for the first window of size 'k'
        for (int i = 0; i < k; i++) {
            currentSum += calories[i];
        }

        // Check the score for the first window
        if (currentSum < lower) {
            score--;
        } else if (currentSum > upper) {
            score++;
        }

        // Slide the window across the array
        for (int i = k; i < calories.length; i++) {
            currentSum += calories[i] - calories[i - k];  // Update the window sum

            // Check the score for the current window
            if (currentSum < lower) {
                score--;
            } else if (currentSum > upper) {
                score++;
            }
        }

        return score;
    }
}
