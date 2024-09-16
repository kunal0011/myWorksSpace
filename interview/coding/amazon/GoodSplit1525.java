package amazon;

 import java.util.HashMap;
        import java.util.Map;

public class GoodSplit1525 {
    public int numSplits(String s) {
        Map<Character, Integer> leftCount = new HashMap<>();
        Map<Character, Integer> rightCount = new HashMap<>();

        // Step 1: Count distinct characters for the right part (initially the whole string)
        for (char ch : s.toCharArray()) {
            rightCount.put(ch, rightCount.getOrDefault(ch, 0) + 1);
        }

        int leftDistinct = 0;
        int rightDistinct = rightCount.size();
        int goodSplits = 0;

        // Step 2: Iterate through the string
        for (char ch : s.toCharArray()) {
            // Add current character to the left part
            leftCount.put(ch, leftCount.getOrDefault(ch, 0) + 1);
            if (leftCount.get(ch) == 1) {
                leftDistinct++;
            }

            // Remove current character from the right part
            rightCount.put(ch, rightCount.get(ch) - 1);
            if (rightCount.get(ch) == 0) {
                rightDistinct--;
            }

            // Compare distinct counts
            if (leftDistinct == rightDistinct) {
                goodSplits++;
            }
        }

        return goodSplits;
    }

    // Testing
    public static void main(String[] args) {
        GoodSplit1525 solution = new GoodSplit1525();
        String s = "aacaba";
        System.out.println("Java Test Result: " + solution.numSplits(s));  // Output should be 2
    }
}

