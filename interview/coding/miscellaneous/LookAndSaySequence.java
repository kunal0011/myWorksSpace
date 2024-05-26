package miscellaneous;
public class LookAndSaySequence {

    public static String nextTerm(String term) {
        StringBuilder next = new StringBuilder();
        int count = 1;
        char digit = term.charAt(0);

        for (int i = 1; i < term.length(); i++) {
            if (term.charAt(i) == digit) {
                // Increment the count if the current digit is the same as the previous one
                count++;
            } else {
                // Append the count and the digit to the next term, then reset the count and update the digit
                next.append(count).append(digit);
                digit = term.charAt(i);
                count = 1;
            }
        }

        // Append the final count and digit
        next.append(count).append(digit);
        return next.toString();
    }

    public static String generateSequence(int n) {
        if (n <= 0) {
            return "";
        }

        String term = "1";
        StringBuilder sequence = new StringBuilder(term);

        for (int i = 1; i < n; i++) {
            term = nextTerm(term);
            sequence.append(", ").append(term);
        }

        return sequence.toString();
    }

    public static void main(String[] args) {
        int terms = 10;
        System.out.println("Look and Say Sequence up to term " + terms + ":");
        System.out.println(generateSequence(terms));
    }
}

