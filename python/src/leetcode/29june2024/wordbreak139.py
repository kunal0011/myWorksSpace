from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # Convert list to set for O(1) look-ups
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string can be segmented

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[len(s)]


sol = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(sol.wordBreak(s, wordDict))  # Output: True
