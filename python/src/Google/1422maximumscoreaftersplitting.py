class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1, len(s)):
            left_score = s[:i].count('0')
            right_score = s[i:].count('1')
            max_score = max(max_score, left_score + right_score)
        return max_score
