class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = list(range(n))
        original = list(range(n))
        count = 0

        while True:
            new_perm = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    new_perm[i] = perm[i // 2]
                else:
                    new_perm[i] = perm[n // 2 + (i - 1) // 2]

            count += 1
            perm = new_perm

            # Check if the permutation is back to the original
            if perm == original:
                break

        return count
