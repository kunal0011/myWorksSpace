package miscellaneous;

public class ReverseBits {
    public static int reverseBits(int n) {
        int result = 0;

        // Iterate through all 32 bits of the integer
       while(n>0) {
            // Left shift result to make space for the next bit
            result <<= 1;

            // Add the least significant bit of n to result
            if ((n & 1) == 1) {
                result |= 1;
            }

            // Right shift n to process the next bit
            n >>= 1;
        }

        return result;
    }

    public static void main(String[] args) {
      //  int num = 43261596;
        // Example number: 00000010100101000001111010011100 in binary
        int num = 11;
        int reversed = reverseBits(num);
        System.out.println("Original: " + Integer.toBinaryString(num));
        System.out.println("Reversed: " + Integer.toBinaryString(reversed));
        System.out.println("Reversed (decimal): " + reversed);
    }
}
