package amazon;

public class SumOfDigitsInMinimumNumber1085 {
    public int sumOfDigits(int[] A) {
        // Step 1: Find the minimum number in the array
        int minNum = Integer.MAX_VALUE;
        for (int num : A) {
            if (num < minNum) {
                minNum = num;
            }
        }

        // Step 2: Calculate the sum of its digits
        int digitSum = 0;
        while (minNum > 0) {
            digitSum += minNum % 10; // Add the last digit
            minNum /= 10;            // Remove the last digit
        }

        // Step 3: Return 1 if the sum is even, 0 if odd
        return digitSum % 2 == 0 ? 1 : 0;
    }
}

