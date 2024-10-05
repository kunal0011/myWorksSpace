class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Convert wordDict to a set for faster lookup
        word_set = set(wordDict)

        # DP array where dp[i] is True if s[0:i] can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: an empty string can be segmented

        # Iterate through the string and populate the dp array
        for i in range(1, len(s) + 1):
            for j in range(i):
                # Check if the substring s[j:i] is in the dictionary and dp[j] is True
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]
