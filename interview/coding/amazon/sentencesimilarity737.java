package amazon;

import java.util.*;

class UnionFind {
    private Map<String, String> parent;

    public UnionFind() {
        this.parent = new HashMap<>();
    }

    public String find(String word) {
        if (!parent.containsKey(word)) {
            parent.put(word, word);
        }
        if (!word.equals(parent.get(word))) {
            parent.put(word, find(parent.get(word)));  // Path compression
        }
        return parent.get(word);
    }

    public void union(String word1, String word2) {
        String root1 = find(word1);
        String root2 = find(word2);
        if (!root1.equals(root2)) {
            parent.put(root2, root1);
        }
    }
}

public class sentencesimilarity737 {
    public boolean areSentencesSimilarTwo(String[] words1, String[] words2, List<List<String>> pairs) {
        if (words1.length != words2.length) {
            return false;
        }

        UnionFind721 uf = new UnionFind721();

        // Union all word pairs
        for (List<String> pair : pairs) {
            uf.union(pair.get(0), pair.get(1));
        }

        // Check if each word in words1 is similar to the corresponding word in words2
        for (int i = 0; i < words1.length; i++) {
            if (!uf.find(words1[i]).equals(uf.find(words2[i]))) {
                return false;
            }
        }

        return true;
    }

    // Test the function
    public static void main(String[] args) {
        sentencesimilarity737 sol = new sentencesimilarity737();

        // Test case 1
        String[] words1_1 = {"great", "acting", "skills"};
        String[] words2_1 = {"fine", "drama", "talent"};
        List<List<String>> pairs_1 = Arrays.asList(
                Arrays.asList("great", "good"),
                Arrays.asList("fine", "good"),
                Arrays.asList("acting", "drama"),
                Arrays.asList("skills", "talent")
        );
        System.out.println(sol.areSentencesSimilarTwo(words1_1, words2_1, pairs_1));  // Output: True

        // Test case 2
        String[] words1_2 = {"great"};
        String[] words2_2 = {"great"};
        List<List<String>> pairs_2 = Collections.emptyList();
        System.out.println(sol.areSentencesSimilarTwo(words1_2, words2_2, pairs_2));  // Output: True

        // Test case 3
        String[] words1_3 = {"great"};
        String[] words2_3 = {"fine"};
        List<List<String>> pairs_3 = Arrays.asList(
                Arrays.asList("great", "good"),
                Arrays.asList("fine", "good")
        );
        System.out.println(sol.areSentencesSimilarTwo(words1_3, words2_3, pairs_3));  // Output: True
    }
}
