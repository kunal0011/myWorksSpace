from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1

        trust_scores = [0] * (n + 1)

        # Process the trust array
        for a, b in trust:
            trust_scores[a] -= 1  # a trusts someone
            trust_scores[b] += 1  # b is trusted

        # Check if there's a person with score n-1 (the judge)
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i

        return -1


# Testing
solution = Solution()
n = 3
trust = [[1, 3], [2, 3]]
print("Python Test Result:", solution.findJudge(n, trust))  # Output: 3
