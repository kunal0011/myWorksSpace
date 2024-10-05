class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []

        # Find factors up to √n
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)  # i is a factor
                if i != n // i:
                    # n // i is also a factor (unless it's a duplicate)
                    factors.append(n // i)

        # Sort the factors list
        factors.sort()

        # If k is within the range of factors, return the k-th factor (1-indexed)
        if k <= len(factors):
            return factors[k - 1]
        else:
            return -1
