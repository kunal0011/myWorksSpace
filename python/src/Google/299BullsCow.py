from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        # Counters for unmatched digits
        secret_count = Counter()
        guess_count = Counter()

        # First pass to count bulls and collect unmatched digit frequencies
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] += 1
                guess_count[g] += 1

        # Second pass to count cows based on the minimum frequency of each digit
        for digit in guess_count:
            if digit in secret_count:
                cows += min(secret_count[digit], guess_count[digit])

        return f"{bulls}A{cows}B"
