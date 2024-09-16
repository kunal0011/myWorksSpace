package amazon;

public class RemoveOccurance1910 {
    public String removeOccurrences(String s, String part) {
        // Keep removing the substring 'part' from 's' until it no longer appears
        while (s.contains(part)) {
            s = s.replaceFirst(part, "");  // Replace only one occurrence at a time
        }
        return s;
    }

    // Testing the solution
    public static void main(String[] args) {
        RemoveOccurance1910 solution = new RemoveOccurance1910();

        // Test case
        String s = "daabcbaabcbc";
        String part = "abc";
        System.out.println("Final string: " + solution.removeOccurrences(s, part));  // Expected output: "dab"
    }
}

