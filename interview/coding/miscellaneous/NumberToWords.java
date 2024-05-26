package miscellaneous;

public class NumberToWords {

    private static final String[] belowTen = {
            "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    };

    private static final String[] belowTwenty = {
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    };

    private static final String[] belowHundred = {
            "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    };

    public static String numberToWords(int num) {
        if (num == 0) {
            return "zero";
        }
        return convert(num);
    }

    private static String convert(int num) {
        StringBuilder sb = new StringBuilder();

        if (num >= 10000000) { // Crores
            sb.append(convert(num / 10000000)).append(" crore ");
            num %= 10000000;
        }
        if (num >= 100000) { // Lakhs
            sb.append(convert(num / 100000)).append(" lakh ");
            num %= 100000;
        }
        if (num >= 1000) { // Thousands
            sb.append(convert(num / 1000)).append(" thousand ");
            num %= 1000;
        }
        if (num >= 100) { // Hundreds
            sb.append(convert(num / 100)).append(" hundred ");
            num %= 100;
        }
        if (num > 0) {
            if (num < 10) {
                sb.append(belowTen[num]);
            } else if (num < 20) {
                sb.append(belowTwenty[num - 10]);
            } else {
                sb.append(belowHundred[num / 10]).append(" ").append(belowTen[num % 10]);
            }
        }

        return sb.toString().trim();
    }

    public static void main(String[] args) {
        int input = 438237719;
        String result = numberToWords(input);
        System.out.println("Output: " + result);
    }
}
