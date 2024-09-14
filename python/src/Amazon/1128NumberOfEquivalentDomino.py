from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        # Dictionary to count occurrences of each normalized domino
        count = defaultdict(int)

        # Normalize and count each domino
        for a, b in dominoes:
            normalized = tuple(sorted([a, b]))
            count[normalized] += 1

        # Calculate number of equivalent pairs
        result = 0
        for freq in count.values():
            if freq > 1:
                result += freq * (freq - 1) // 2

        return result
