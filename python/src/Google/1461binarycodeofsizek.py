class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required = 1 << k  # Total number of binary codes of length k
        seen = set()

        for i in range(k, len(s) + 1):
            seen.add(s[i-k:i])
            if len(seen) == required:
                return True
        return False
