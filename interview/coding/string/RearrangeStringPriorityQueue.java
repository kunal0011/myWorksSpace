package string;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class RearrangeStringPriorityQueue {
    public static String rearrangeString(String str) {
        if (str == null || str.isEmpty()) {
            return str;
        }

        // Step 1: Create frequency map of characters
        Map<Character, Integer> frequencyMap = new HashMap<>();
        for (char c : str.toCharArray()) {
            frequencyMap.put(c, frequencyMap.getOrDefault(c, 0) + 1);
        }

        // Step 2: Create priority queue (max heap) based on character frequencies
        PriorityQueue<Character> maxHeap = new PriorityQueue<>((a, b) -> frequencyMap.get(b) - frequencyMap.get(a));
        maxHeap.addAll(frequencyMap.keySet());

        // Step 3-5: Rearrange characters in the result string
        StringBuilder result = new StringBuilder();
        char lastChar = '\0'; // Placeholder for the last character inserted
        while (!maxHeap.isEmpty()) {
            char currentChar = maxHeap.poll();
            // If the current character is the same as the last inserted character, find the next character
            while (currentChar == lastChar && !maxHeap.isEmpty()) {
                char temp = currentChar;
                currentChar = maxHeap.poll();
                maxHeap.offer(temp); // Put back the character in the queue
            }
            if (currentChar != lastChar) {
                result.append(currentChar);
                frequencyMap.put(currentChar, frequencyMap.get(currentChar) - 1);
                if (frequencyMap.get(currentChar) > 0) {
                    maxHeap.offer(currentChar);
                }
                lastChar = currentChar;
            } else {
                // If no suitable character is found, return an empty string
                return "";
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        String input = "aaabc";
        System.out.println("Original string: " + input);
        System.out.println("Rearranged string: " + rearrangeString(input));
    }
}
