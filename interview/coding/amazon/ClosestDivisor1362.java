package amazon;

public class ClosestDivisor1362 {
    // Helper function to find divisors of a number
    public int[] findDivisors(int x) {
        for (int i = (int) Math.sqrt(x); i > 0; i--) {
            if (x % i == 0) {
                return new int[]{i, x / i};
            }
        }
        return new int[]{};
    }

    public int[] closestDivisors(int num) {
        // Find divisors for num+1 and num+2
        int[] divisors1 = findDivisors(num + 1);
        int[] divisors2 = findDivisors(num + 2);

        // Return the pair with the smaller difference between the divisors
        if (Math.abs(divisors1[1] - divisors1[0]) < Math.abs(divisors2[1] - divisors2[0])) {
            return divisors1;
        } else {
            return divisors2;
        }
    }
}
