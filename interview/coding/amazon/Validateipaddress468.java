package amazon;

public class Validateipaddress468 {
    public String validIPAddress(String queryIP) {
        if (queryIP.chars().filter(ch -> ch == '.').count() == 3) {
            return isIPv4(queryIP) ? "IPv4" : "Neither";
        } else if (queryIP.chars().filter(ch -> ch == ':').count() == 7) {
            return isIPv6(queryIP) ? "IPv6" : "Neither";
        } else {
            return "Neither";
        }
    }

    private boolean isIPv4(String s) {
        String[] parts = s.split("\\.", -1); // Use -1 to prevent ignoring trailing empty parts
        if (parts.length != 4) {
            return false;
        }
        for (String part : parts) {
            // Check if it's a valid number between 0 and 255 without leading zeros
            if (part.length() == 0 || part.length() > 3 || (part.charAt(0) == '0' && part.length() > 1)) {
                return false;
            }
            try {
                int num = Integer.parseInt(part);
                if (num < 0 || num > 255) {
                    return false;
                }
            } catch (NumberFormatException e) {
                return false;
            }
        }
        return true;
    }

    private boolean isIPv6(String s) {
        String[] parts = s.split(":", -1);
        if (parts.length != 8) {
            return false;
        }
        String hexDigits = "0123456789abcdefABCDEF";
        for (String part : parts) {
            // Each part must be between 1 and 4 hexadecimal digits
            if (part.length() == 0 || part.length() > 4) {
                return false;
            }
            for (char c : part.toCharArray()) {
                if (hexDigits.indexOf(c) == -1) {
                    return false;
                }
            }
        }
        return true;
    }

    // Test cases
    public static void main(String[] args) {
        Validateipaddress468 sol = new Validateipaddress468();

        // Test case 1
        String queryIP1 = "172.16.254.1";
        System.out.println(sol.validIPAddress(queryIP1));  // Expected output: "IPv4"

        // Test case 2
        String queryIP2 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334";
        System.out.println(sol.validIPAddress(queryIP2));  // Expected output: "IPv6"

        // Test case 3
        String queryIP3 = "256.256.256.256";
        System.out.println(sol.validIPAddress(queryIP3));  // Expected output: "Neither"
    }
}
