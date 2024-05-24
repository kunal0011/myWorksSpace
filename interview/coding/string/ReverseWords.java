package string;

public class ReverseWords {

    // Method to reverse words in a given string
    public static String reverseWords(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }

        // Split the string by spaces to get the words
        String[] words = s.split(" ");

        // Use StringBuilder for efficient string manipulation
        StringBuilder reversedString = new StringBuilder();

        // Loop through the words array from the end to the beginning
        for (int i = words.length - 1; i >= 0; i--) {
            // Skip empty words (possible due to multiple spaces)
            if (!words[i].isEmpty()) {
                reversedString.append(words[i]).append(" ");
            }
        }

        // Remove the trailing space and return the result
        return reversedString.toString().trim();
    }

    public static void main(String[] args) {
        String input = "The quick brown fox jumps over the lazy dog";
        String output = reverseWords(input);
        System.out.println("Original: " + input);
        System.out.println("Reversed: " + output);
    }
}
