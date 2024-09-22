package amazon;

public class ConvettoHex405 {
    public String toHex(int num) {
        if (num == 0) {
            return "0";
        }

        char[] hexChars = "0123456789abcdef".toCharArray();
        StringBuilder result = new StringBuilder();

        // Convert to 32-bit unsigned
        num &= 0xFFFFFFFF;

        while (num > 0) {
            result.append(hexChars[num % 16]);
            num /= 16;
        }

        return result.reverse().toString();
    }

    public static void main(String[] args) {
        ConvettoHex405 sol = new ConvettoHex405();
        System.out.println(sol.toHex(26));    // Expected output: "1a"
        System.out.println(sol.toHex(-1));    // Expected output: "ffffffff"
        System.out.println(sol.toHex(0));     // Expected output: "0"
    }
}

