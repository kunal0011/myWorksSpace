package amazon;

import java.util.ArrayList;
import java.util.List;

public class Indexpait1065 {
    public int[][] indexPairs(String text, String[] words) {
        List<int[]> result = new ArrayList<>();

        // For each word in words, find its occurrences in the text
        for (String word : words) {
            int start = text.indexOf(word);
            while (start != -1) {
                // Add the index pair [start, start + word.length() - 1]
                result.add(new int[]{start, start + word.length() - 1});
                // Look for the next occurrence of the word
                start = text.indexOf(word, start + 1);
            }
        }

        // Convert the result list to an array
        result.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        return result.toArray(new int[result.size()][]);
    }
}
