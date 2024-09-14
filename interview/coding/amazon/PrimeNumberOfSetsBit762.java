package amazon;

import java.util.HashSet;
import java.util.Set;

public class PrimeNumberOfSetsBit762 {
    private Set<Integer> primes;

    public PrimeNumberOfSetsBit762() {
        primes = new HashSet<>();
        // Calculate all primes up to 32
        boolean[] isPrime = new boolean[33];
        for (int i = 2; i < isPrime.length; i++) isPrime[i] = true;
        for (int p = 2; p * p < isPrime.length; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i < isPrime.length; i += p) {
                    isPrime[i] = false;
                }
            }
        }
        for (int i = 2; i < isPrime.length; i++) {
            if (isPrime[i]) primes.add(i);
        }
    }

    public int countPrimeSetBits(int L, int R) {
        int count = 0;
        for (int num = L; num <= R; num++) {
            int setBits = Integer.bitCount(num);
            if (primes.contains(setBits)) {
                count++;
            }
        }
        return count;
    }
}
