package miscellaneous;

public class PossibleStringsByPlacingSpaces {

    public static void printAllPossibleStrings(String input) {
        if (input == null || input.isEmpty()) {
            return;
        }
        printAllPossibleStringsRecursive(input, 0, "");
    }

    private static void printAllPossibleStringsRecursive(String input, int index, String output) {
        if (index == input.length()) {
            System.out.println(output);
            return;
        }

        // Append the current character without a space
        printAllPossibleStringsRecursive(input, index + 1, output + input.charAt(index));

        // Append the current character with a space
        if (index < input.length() - 1) {
            printAllPossibleStringsRecursive(input, index + 1, output + input.charAt(index) + " ");
        }
    }

    public static void main(String[] args) {
        String input = "ABCD";
        System.out.println("All possible strings by placing spaces:");
        printAllPossibleStrings(input);
    }
}

