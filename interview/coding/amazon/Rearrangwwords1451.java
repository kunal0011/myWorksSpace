package amazon;

 import java.util.*;

public class Rearrangwwords1451 {
    public String rearrangeWords(String text) {
        String[] words = text.split(" ");
        List<String> wordList = new ArrayList<>(Arrays.asList(words));

        // Sort words by their length, stable sort keeps the original order for equal lengths
        wordList.sort(Comparator.comparingInt(String::length));

        // Join the sorted words and capitalize the first letter
        String rearrangedSentence = String.join(" ", wordList);
        return Character.toUpperCase(rearrangedSentence.charAt(0)) + rearrangedSentence.substring(1);
    }

    // Testing
    public static void main(String[] args) {
        Rearrangwwords1451 solution = new Rearrangwwords1451();
        String text = "The quick brown fox jumps over the lazy dog";
        System.out.println("Java Test Result: " + solution.rearrangeWords(text));  // Output should be "The fox the dog over brown quick jumps lazy"
    }
}
