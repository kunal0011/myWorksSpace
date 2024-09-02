from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(
            enumerate(score), key=lambda x: x[1], reverse=True)
        result = [""] * len(score)

        for i, (index, _) in enumerate(sorted_score):
            if i == 0:
                result[index] = "Gold Medal"
            elif i == 1:
                result[index] = "Silver Medal"
            elif i == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(i + 1)

        return result
