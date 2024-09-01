class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0

        # Consider each possible starting point for the substring
        for i in range(len(s)):
            # To store the frequency of each character in the current substring
            freq = [0] * 26

            # Consider each possible ending point for the substring
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('a')] += 1

                max_freq = max(freq)
                min_freq = min(f for f in freq if f > 0)

                # Calculate beauty of the current substring and add it to total_beauty
                total_beauty += (max_freq - min_freq)

        return total_beauty
