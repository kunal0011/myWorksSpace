class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        size = len(s)
        first_group = size % k

        parts = []
        if first_group:
            parts.append(s[:first_group])

        for i in range(first_group, size, k):
            parts.append(s[i:i+k])

        return "-".join(parts)
