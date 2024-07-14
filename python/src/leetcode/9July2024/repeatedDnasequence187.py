from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        seen, repeated = {}, set()

        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in seen:
                repeated.add(substring)
            else:
                seen[substring] = 1

        return list(repeated)


# Example usage
sol = Solution()
dna_sequence = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result = sol.findRepeatedDnaSequences(dna_sequence)
print(result)
