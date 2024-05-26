package miscellaneous;

public class MagicNumber {
    public static int nthMagicNumber(int n) {
        int magicNumber = 0;
        int power = 1; // Represents 5^0 initially

        while (n > 0) {
            if ((n & 1) == 1) {
                magicNumber += power;
            }
            power *= 5;
            n >>= 1;
        }

        return magicNumber;
    }

    public static void main(String[] args) {
        int n = 5;
        System.out.println(n + "th magic number is: " + nthMagicNumber(n)); // Output: 26

        n = 10;
        System.out.println(n + "th magic number is: " + nthMagicNumber(n)); // Output: 130
    }
}
