package amazon;

public class Reverseletters917 {
    public String reverseOnlyLetters(String S) {
        char[] chars = S.toCharArray();
        int left = 0, right = S.length() - 1;

        while (left < right) {
            if (!Character.isLetter(chars[left])) {
                left++;
            } else if (!Character.isLetter(chars[right])) {
                right--;
            } else {
                // Swap letters
                char temp = chars[left];
                chars[left] = chars[right];
                chars[right] = temp;
                left++;
                right--;
            }
        }

        return new String(chars);
    }

    // Test cases
    public static void main(String[] args) {
        Reverseletters917 sol = new Reverseletters917();

        // Test case 1
        String S1 = "ab-cd";
        System.out.println(sol.reverseOnlyLetters(S1));  // Expected output: "dc-ba"

        // Test case 2
        String S2 = "a-bC-dEf-ghIj";
        System.out.println(sol.reverseOnlyLetters(S2));  // Expected output: "j-Ih-gfE-dCba"

        // Test case 3
        String S3 = "Test1ng-Leet=code-Q!";
        System.out.println(sol.reverseOnlyLetters(S3));  // Expected output: "Qedo1ct-eeLg=ntseT!"
    }
}

