package amazon;

import java.math.BigInteger;

public class PrimeArrangement1175 {
    private static final int MOD = 1000000007;

    public int numPrimeArrangements(int n) {
        // Helper function to determine if a number is prime
        boolean[] isPrime = new boolean[n + 1];
        int primeCount = 0;

        // Find prime numbers using the sieve method
        for (int i = 2; i <= n; i++) {
            isPrime[i] = true;
        }
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        // Count prime numbers
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                primeCount++;
            }
        }

        int nonPrimeCount = n - primeCount;

        // Return the factorial of primeCount and nonPrimeCount modulo MOD
        return factorial(primeCount).multiply(factorial(nonPrimeCount)).mod(BigInteger.valueOf(MOD)).intValue();
    }

    // Helper function to compute factorial modulo MOD
    private BigInteger factorial(int num) {
        BigInteger result = BigInteger.ONE;
        for (int i = 2; i <= num; i++) {
            result = result.multiply(BigInteger.valueOf(i));
        }
        return result;
    }

    // Test cases
    public static void main(String[] args) {
        PrimeArrangement1175 sol = new PrimeArrangement1175();

        // Test case 1
        int n1 = 5;
        int result1 = sol.numPrimeArrangements(n1);
        assert result1 == 12 : "Test case 1 failed: " + result1;

        // Test case 2
        int n2 = 100;
        int result2 = sol.numPrimeArrangements(n2);
        assert result2 == 682289015 : "Test case 2 failed: " + result2;

        System.out.println("All test cases passed!");
    }
}
