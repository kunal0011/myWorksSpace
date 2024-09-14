package amazon;

public class Armstronnumber1134 {
    public boolean isArmstrong(int n) {
        // Convert the number to a string to find the digits
        String numStr = Integer.toString(n);
        int numDigits = numStr.length();
        int armstrongSum = 0;

        // Calculate the sum of each digit raised to the power of the number of digits
        for (int i = 0; i < numDigits; i++) {
            int digit = Character.getNumericValue(numStr.charAt(i));
            armstrongSum += Math.pow(digit, numDigits);
        }

        // Check if the sum equals the original number
        return armstrongSum == n;
    }
}
