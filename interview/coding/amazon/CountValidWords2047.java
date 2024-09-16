package amazon;

public class CountValidWords2047 {
    public int countValidWords(String sentence) {
        String[] words = sentence.split("\\s+");
        int validCount = 0;

        for (String word : words) {
            if (isValid(word)) {
                validCount++;
            }
        }

        return validCount;
    }

    private boolean isValid(String word) {
        return word.matches("^[a-z]*([a-z]-[a-z])?[a-z]*[!.,]?$");
    }

    // Testing the solution
    public static void main(String[] args) {
        CountValidWords2047 solution = new CountValidWords2047();

        // Test case
        String sentence = "cat and  dog";
        System.out.println("Valid Words Count: " + solution.countValidWords(sentence));  // Expected output: 3
    }
}

