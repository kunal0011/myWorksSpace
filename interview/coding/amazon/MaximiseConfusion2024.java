package amazon;

public class MaximiseConfusion2024 {

    public int maxConsecutiveChar(String answerKey, char ch, int k) {
        int left = 0;
        int flips = 0;
        int maxLen = 0;

        for (int right = 0; right < answerKey.length(); right++) {
            if (answerKey.charAt(right) != ch) {
                flips++;
            }

            while (flips > k) {
                if (answerKey.charAt(left) != ch) {
                    flips--;
                }
                left++;
            }

            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
    public int maxConsecutiveAnswers(String answerKey, int k) {
        // Helper function to maximize consecutive occurrences of a given character


        // Maximize consecutive 'T's or 'F's
        return Math.max(maxConsecutiveChar(answerKey,'T',k), maxConsecutiveChar(answerKey,'F',k));
    }

    // Testing the solution
    public static void main(String[] args) {
        MaximiseConfusion2024 solution = new MaximiseConfusion2024();

        // Test case
        String answerKey = "TTFF";
        int k = 2;
        System.out.println("Maximum consecutive identical answers: " + solution.maxConsecutiveAnswers(answerKey, k));  // Expected output: 4
    }
}

