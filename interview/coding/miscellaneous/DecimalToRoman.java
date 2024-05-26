package miscellaneous;

public class DecimalToRoman {

    public static String intToRoman(int num) {
        // Define the values and their corresponding Roman numeral strings
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] romanNumerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder result = new StringBuilder();

        // Construct the Roman numeral
        for (int i = 0; i < values.length; i++) {
            while (num >= values[i]) {
                num -= values[i];
                result.append(romanNumerals[i]);
            }
        }

        return result.toString();
    }

    public static void main(String[] args) {
        // Test the function with different numbers
        int[] testNumbers = {3, 58, 1994, 438237764}; // Example input
        for (int number : testNumbers) {
            System.out.println(number + " -> " + intToRoman(number));
        }
    }
}
