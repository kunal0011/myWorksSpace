class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check if there's more than 1 'A' or if there are more than 2 consecutive 'L's
        return s.count('A') <= 1 and 'LLL' not in s
