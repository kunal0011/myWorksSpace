"""
LeetCode 506 - Relative Ranks

Problem Statement:
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition.
All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, 
the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
- The 1st place athlete's rank is "Gold Medal".
- The 2nd place athlete's rank is "Silver Medal".
- The 3rd place athlete's rank is "Bronze Medal".
- For the 4th place to nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.
"""

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a sorted list of (score, index) pairs in descending order
        score_with_index = [(s, i) for i, s in enumerate(score)]
        score_with_index.sort(reverse=True)

        # Initialize result array
        n = len(score)
        result = [""] * n

        # Assign ranks
        for rank, (_, index) in enumerate(score_with_index):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(rank + 1)

        return result


def run_tests():
    solution = Solution()

    # Test Case 1
    score1 = [5, 4, 3, 2, 1]
    print("Test Case 1:")
    print(f"Input: {score1}")
    print(f"Output: {solution.findRelativeRanks(score1)}")
    # Expected: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

    # Test Case 2
    score2 = [10, 3, 8, 9, 4]
    print("\nTest Case 2:")
    print(f"Input: {score2}")
    print(f"Output: {solution.findRelativeRanks(score2)}")
    # Expected: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

    # Test Case 3
    score3 = [1]
    print("\nTest Case 3:")
    print(f"Input: {score3}")
    print(f"Output: {solution.findRelativeRanks(score3)}")
    # Expected: ["Gold Medal"]


if __name__ == "__main__":
    run_tests()
