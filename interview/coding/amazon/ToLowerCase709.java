package amazon;

public class ToLowerCase709 {
    public String toLowerCase(String s) {
        // Using built-in method
        return s.toLowerCase();
    }

    // Test the function
    public static void main(String[] args) {
        ToLowerCase709 sol = new ToLowerCase709();

        // Test case 1
        String s1 = "Hello";
        System.out.println(sol.toLowerCase(s1));  // Output: "hello"

        // Test case 2
        String s2 = "LOVELY";
        System.out.println(sol.toLowerCase(s2));  // Output: "lovely"

        // Test case 3
        String s3 = "here";
        System.out.println(sol.toLowerCase(s3));  // Output: "here"
    }
}
