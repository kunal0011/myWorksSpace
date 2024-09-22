package amazon;

public class findComplement476 {
    public int findComplement(int num) {
        // Get the bit length of num
        int bitLength = Integer.toBinaryString(num).length();
        // Create a mask with all bits set to 1 (same length as num)
        int mask = (1 << bitLength) - 1;
        // XOR num with the mask to get the complement
        return num ^ mask;
    }

    // Test cases
    public static void main(String[] args) {
        findComplement476 sol = new findComplement476();

        // Test case 1
        int num1 = 5;
        System.out.println(sol.findComplement(num1));  // Expected output: 2

        // Test case 2
        int num2 = 1;
        System.out.println(sol.findComplement(num2));  // Expected output: 0
    }
}

