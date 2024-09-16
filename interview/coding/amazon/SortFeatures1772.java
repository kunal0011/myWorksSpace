package amazon;
//Problem Breakdown:
//        Features: A list of keywords representing product features.
//        Responses: A list of customer feedback strings, where each string may contain multiple words, including features.
//        Task: You need to count the occurrences of each feature in the responses (case-insensitive) and return the features sorted by their frequency. If two features have the same frequency, they should appear in the order they were given in the original feature list.
 import java.util.*;

public class SortFeatures1772 {
    public String[] sortFeatures(String[] features, String[] responses) {
        // Create a map to store the count of each feature
        Map<String, Integer> featureCount = new HashMap<>();
        for (String feature : features) {
            featureCount.put(feature, 0);
        }

        // Count the occurrences of each feature in the responses
        for (String response : responses) {
            Set<String> words = new HashSet<>(Arrays.asList(response.toLowerCase().split("\\s+")));  // Use a set to avoid duplicates
            for (String feature : features) {
                if (words.contains(feature)) {
                    featureCount.put(feature, featureCount.get(feature) + 1);
                }
            }
        }

        // Sort the features by their count (in descending order)
        Arrays.sort(features, (a, b) -> {
            int countA = featureCount.get(a);
            int countB = featureCount.get(b);
            if (countA != countB) {
                return countB - countA;  // Sort by descending count
            }
            return 0;  // Keep the original order if counts are the same
        });

        return features;
    }

    // Testing the solution
    public static void main(String[] args) {
        SortFeatures1772 solution = new SortFeatures1772();

        // Test case
        String[] features = {"cooler", "lock", "touch"};
        String[] responses = {"i like cooler cooler", "lock touch cool", "locker room"};
        System.out.println("Sorted features: " + Arrays.toString(solution.sortFeatures(features, responses)));
        // Expected output: ["cooler", "touch", "lock"]
    }
}
